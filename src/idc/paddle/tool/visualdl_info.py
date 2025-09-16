import argparse
import csv
import datetime
import io
import logging
import sys
import traceback

from wai.logging import init_logging, set_logging_level, add_logging_level
from seppl.placeholders import placeholder_list
from visualdl import LogReader
from idc.core import ENV_IDC_LOGLEVEL

VISUALDL_INFO = "idc-visualdl-info"

_logger = logging.getLogger(VISUALDL_INFO)


INFO_TAGS = "tags"
INFO_DATA = "data"
INFO_TYPES = [
    INFO_TAGS,
    INFO_DATA,
]


def visualdl_info(log_file: str, info_type: str, component: str = None, tag: str = None, logger: logging.Logger = None) -> str:
    """
    Generates information from the visualdl log file and returns it.

    :param log_file: the log file to inspect
    :type log_file: str
    :param info_type: the type of info to generate
    :type info_type: str
    :param component: the component to output, if INFO_COMPONENT
    :type component: str
    :param tag: the tag to output, if INFO_COMPONENT
    :type tag: str
    :param logger: the optional logging instance to use
    :type logger: logging.Logger
    :return: the generated info
    :rtype: str
    """
    if logger is not None:
        logger.info("Loading: %s" % log_file)
    reader = LogReader(file_path=log_file)
    result = ""

    if info_type == INFO_TAGS:
        for tag in reader.get_tags():
            result += tag + "\n"
            items = reader.get_tags()[tag]
            for item in items:
                result += "  " + item + "\n"

    elif info_type == INFO_DATA:
        if (component is None) or (len(component) == 0):
            raise Exception("No component specified!")
        if (tag is None) or (len(tag) == 0):
            raise Exception("No tag specified!")
        if component == "scalar":
            if logger is not None:
                logger.info("Getting data for component/tag: %s/%s" % (component, tag))
            data = reader.get_data(component, tag)
            buffer = io.StringIO()
            writer = csv.writer(buffer, quoting=csv.QUOTE_MINIMAL, delimiter=",")
            writer.writerow(["id", "tag", "timestamp", "value"])
            for row in data:
                writer.writerow([row.id, row.tag, datetime.datetime.fromtimestamp(row.timestamp / 1000.0), row.value])
            result = buffer.getvalue()
        else:
            if logger is not None:
                logger.info("Don't know how to handle component '%s', can only return a simple string representation!" % component)
            data = reader.get_data(component, tag)
            buffer = io.StringIO()
            for row in data:
                buffer.write(str(row))
                buffer.write("\n")
            result = buffer.getvalue()

    else:
        raise Exception("Unhandled info type: %s" % info_type)

    return result


def main(args=None):
    """
    The main method for parsing command-line arguments.

    :param args: the commandline arguments, uses sys.argv if not supplied
    :type args: list
    """
    init_logging(env_var=ENV_IDC_LOGLEVEL)
    parser = argparse.ArgumentParser(
        description="Tool for outputting information on VisualDL log files.",
        prog=VISUALDL_INFO,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--log_file", type=str, help="The log file to read; " + placeholder_list(input_based=False), default=None, required=True)
    parser.add_argument("-i", "--info_type", choices=INFO_TYPES, help="The type of information to generate.", default=INFO_TAGS, required=False)
    parser.add_argument("-c", "--component", type=str, help="The component for which to output the data, e.g., 'scalar'.", default=None, required=False)
    parser.add_argument("-t", "--tag", type=str, help="The tag for which to output the data, e.g., 'Evaluate/mIoU'.", default=None, required=False)
    parser.add_argument("-o", "--output", type=str, help="The file to store the information in rather than outputting it on stdout.", default=None, required=False)
    add_logging_level(parser)
    parsed = parser.parse_args(args=args)
    set_logging_level(_logger, parsed.logging_level)
    info = visualdl_info(parsed.log_file, info_type=parsed.info_type, component=parsed.component, tag=parsed.tag, logger=_logger)
    if parsed.output is None:
        print(info)
    else:
        _logger.info("Saving info to: %s" % parsed.output)
        with open(parsed.output, "w") as fp:
            fp.write(info)


def sys_main() -> int:
    """
    Runs the main function using the system cli arguments, and
    returns a system error code.

    :return: 0 for success, 1 for failure.
    """
    try:
        main()
        return 0
    except Exception:
        traceback.print_exc()
        print("options: %s" % str(sys.argv[1:]), file=sys.stderr)
        return 1


if __name__ == '__main__':
    main()
