import argparse
import os.path
from typing import List, Iterable, Union

from seppl.placeholders import PlaceholderSupporter, placeholder_list
from seppl.io import locate_files
from wai.logging import LOGGING_WARNING

from visualdl import LogReader
from kasperl.api import Reader, XYPlot


class VisualDLReader(Reader, PlaceholderSupporter):

    def __init__(self, source: Union[str, List[str]] = None, source_list: Union[str, List[str]] = None,
                 resume_from: str = None, component: str = None, tag: str = None, use_timestamp: bool = None,
                 logger_name: str = None, logging_level: str = LOGGING_WARNING):
        """
        Initializes the reader.

        :param source: the filename(s)
        :param source_list: the file(s) with filename(s)
        :param resume_from: the file to resume from (glob)
        :type resume_from: str
        :param component: the component to load from the log file
        :type component: str
        :param tag: the tag to load from the log file
        :type tag: str
        :param use_timestamp: whether to use the timestamp rather than the id for the x axis
        :type use_timestamp: bool
        :param logger_name: the name to use for the logger
        :type logger_name: str
        :param logging_level: the logging level to use
        :type logging_level: str
        """
        super().__init__(logger_name=logger_name, logging_level=logging_level)
        self.source = source
        self.source_list = source_list
        self.resume_from = resume_from
        self.component = component
        self.tag = tag
        self.use_timestamp = use_timestamp
        self._inputs = None
        self._current_input = None

    def name(self) -> str:
        """
        Returns the name of the handler, used as sub-command.

        :return: the name
        :rtype: str
        """
        return "from-visualdl"

    def description(self) -> str:
        """
        Returns a description of the reader.

        :return: the description
        :rtype: str
        """
        return "Loads data from a VisualDL log file (e.g., 'scalar' data like 'Evaluate/mIoU') and forwards it as a plot."

    def _create_argparser(self) -> argparse.ArgumentParser:
        """
        Creates an argument parser. Derived classes need to fill in the options.

        :return: the parser
        :rtype: argparse.ArgumentParser
        """
        parser = super()._create_argparser()
        parser.add_argument("-i", "--input", type=str, help="Path to the log file(s) to read; glob syntax is supported; " + placeholder_list(obj=self), required=False, nargs="*")
        parser.add_argument("-I", "--input_list", type=str, help="Path to the text file(s) listing the log files to use; " + placeholder_list(obj=self), required=False, nargs="*")
        parser.add_argument("--resume_from", type=str, help="Glob expression matching the file to resume from, e.g., './vdlrecords.*.log'", required=False)
        parser.add_argument("-c", "--component", type=str, default="scalar", help="The component to load from the log file, e.g., 'scalar'.", required=False)
        parser.add_argument("-t", "--tag", type=str, default=None, help="The tag to load from the log file, e.g., 'Evaluate/mIoU'.", required=True)
        parser.add_argument("-T", "--use_timestamp", action="store_true", help="Whether to use the timestamp instead of the ID for the x axis.")
        return parser

    def _apply_args(self, ns: argparse.Namespace):
        """
        Initializes the object with the arguments of the parsed namespace.

        :param ns: the parsed arguments
        :type ns: argparse.Namespace
        """
        super()._apply_args(ns)
        self.source = ns.input
        self.source_list = ns.input_list
        self.resume_from = ns.resume_from
        self.component = ns.component
        self.tag = ns.tag
        self.use_timestamp = ns.use_timestamp

    def generates(self) -> List:
        """
        Returns the list of classes that get produced.

        :return: the list of classes
        :rtype: list
        """
        return [XYPlot]

    def initialize(self):
        """
        Initializes the processing, e.g., for opening files or databases.
        """
        super().initialize()

        if self.component is None:
            self.component = "scalar"
        if self.tag is None:
            raise Exception("No tag specified!")
        if self.use_timestamp is None:
            self.use_timestamp = False

        self._inputs = None

    def read(self) -> Iterable:
        """
        Loads the data and returns the items one by one.

        :return: the data
        :rtype: Iterable
        """
        if self._inputs is None:
            self._inputs = locate_files(self.source, input_lists=self.source_list, fail_if_empty=True, default_glob="*.log", resume_from=self.resume_from)
        self._current_input = self._inputs.pop(0)
        self.session.current_input = self._current_input
        self.logger().info("Reading from: " + str(self.session.current_input))
        reader = LogReader(file_path=self.session.current_input)
        self.logger().info("Loading component/tag: %s/%s" % (self.component, self.tag))
        data = reader.get_data(self.component, self.tag)
        x = []
        y = []
        for item in data:
            if self.use_timestamp:
                x.append(item.timestamp / 1000.0)
            else:
                x.append(item.id)
            y.append(item.value)
        yield XYPlot(
            title=os.path.basename(self.session.current_input),
            x_data=x, x_label=("timestamp" if self.use_timestamp else "step"),
            y_data=y, y_label=self.tag)

    def has_finished(self) -> bool:
        """
        Returns whether reading has finished.

        :return: True if finished
        :rtype: bool
        """
        return len(self._inputs) == 0
