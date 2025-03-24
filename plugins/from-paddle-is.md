# from-paddle-is

* generates: idc.api.ImageSegmentationData

Loads the image segmentation from the specified text files listing image (JPG with relative path) and annotation image (indexed PNG with relative path). The labels (incl background) are specified via a separate text file.

```
usage: from-paddle-is [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                      [-N LOGGER_NAME] [-i [INPUT ...]] [-I [INPUT_LIST ...]]
                      [--resume_from RESUME_FROM] [--labels_file FILE]
                      [--labels [LABEL ...]]

Loads the image segmentation from the specified text files listing image (JPG
with relative path) and annotation image (indexed PNG with relative path). The
labels (incl background) are specified via a separate text file.

options:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
  -N LOGGER_NAME, --logger_name LOGGER_NAME
                        The custom name to use for the logger, uses the plugin
                        name by default (default: None)
  -i [INPUT ...], --input [INPUT ...]
                        Path to the text file(s) to read; glob syntax is
                        supported; Supported placeholders: {HOME}, {CWD},
                        {TMP} (default: None)
  -I [INPUT_LIST ...], --input_list [INPUT_LIST ...]
                        Path to the text file(s) listing the text files to
                        use; Supported placeholders: {HOME}, {CWD}, {TMP}
                        (default: None)
  --resume_from RESUME_FROM
                        Glob expression matching the file to resume from,
                        e.g., '*/012345.txt' (default: None)
  --labels_file FILE    The file with the labels associated with the indices
                        (incl. background); Supported placeholders: {HOME},
                        {CWD}, {TMP} (default: None)
  --labels [LABEL ...]  The labels that the indices represent (incl
                        background). (default: None)
```

Available placeholders:

* `{HOME}`: The home directory of the current user.
* `{CWD}`: The current working directory.
* `{TMP}`: The temp directory.
