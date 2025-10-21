# from-visualdl

* generates: kasperl.api.XYPlot

Loads data from a VisualDL log file (e.g., 'scalar' data like 'Evaluate/mIoU') and forwards it as a plot.

```
usage: from-visualdl [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                     [-N LOGGER_NAME] [-i [INPUT ...]] [-I [INPUT_LIST ...]]
                     [--resume_from RESUME_FROM] [-c COMPONENT] -t TAG [-T]

Loads data from a VisualDL log file (e.g., 'scalar' data like 'Evaluate/mIoU')
and forwards it as a plot.

options:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
  -N LOGGER_NAME, --logger_name LOGGER_NAME
                        The custom name to use for the logger, uses the plugin
                        name by default (default: None)
  -i [INPUT ...], --input [INPUT ...]
                        Path to the log file(s) to read; glob syntax is
                        supported; Supported placeholders: {HOME}, {CWD},
                        {TMP} (default: None)
  -I [INPUT_LIST ...], --input_list [INPUT_LIST ...]
                        Path to the text file(s) listing the log files to use;
                        Supported placeholders: {HOME}, {CWD}, {TMP} (default:
                        None)
  --resume_from RESUME_FROM
                        Glob expression matching the file to resume from,
                        e.g., './vdlrecords.*.log' (default: None)
  -c COMPONENT, --component COMPONENT
                        The component to load from the log file, e.g.,
                        'scalar'. (default: scalar)
  -t TAG, --tag TAG     The tag to load from the log file, e.g.,
                        'Evaluate/mIoU'. (default: None)
  -T, --use_timestamp   Whether to use the timestamp instead of the ID for the
                        x axis. (default: False)
```

Available placeholders:

* `{HOME}`: The home directory of the current user.
* `{CWD}`: The current working directory.
* `{TMP}`: The temp directory.
