# from-paddle-is

* generates: idc.api.ImageSegmentationData

Loads the image segmentation from the specified text files listing image (JPG with relative path) and annotation image (indexed PNG with relative path). The labels (incl background) are specified via a separate text file.

```
usage: from-paddle-is [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                      [-N LOGGER_NAME] [-i [INPUT ...]] [-I [INPUT_LIST ...]]
                      [--resume_from RESUME_FROM] [--labels_file FILE]
                      [--labels [LABEL ...]] [--separator SEP]

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
                        {TMP}, {INPUT_PATH}, {INPUT_NAMEEXT},
                        {INPUT_NAMENOEXT}, {INPUT_EXT}, {INPUT_PARENT_PATH},
                        {INPUT_PARENT_NAME} (default: None)
  -I [INPUT_LIST ...], --input_list [INPUT_LIST ...]
                        Path to the text file(s) listing the text files to
                        use; Supported placeholders: {HOME}, {CWD}, {TMP},
                        {INPUT_PATH}, {INPUT_NAMEEXT}, {INPUT_NAMENOEXT},
                        {INPUT_EXT}, {INPUT_PARENT_PATH}, {INPUT_PARENT_NAME}
                        (default: None)
  --resume_from RESUME_FROM
                        Glob expression matching the file to resume from,
                        e.g., '*/012345.txt' (default: None)
  --labels_file FILE    The file with the labels associated with the indices
                        (incl. background); Supported placeholders: {HOME},
                        {CWD}, {TMP}, {INPUT_PATH}, {INPUT_NAMEEXT},
                        {INPUT_NAMENOEXT}, {INPUT_EXT}, {INPUT_PARENT_PATH},
                        {INPUT_PARENT_NAME} (default: None)
  --labels [LABEL ...]  The labels that the indices represent (incl
                        background). (default: None)
  --separator SEP       The separator to use for reading the text files.
                        (default: )
```

Available placeholders:

* `{HOME}`: The home directory of the current user.
* `{CWD}`: The current working directory.
* `{TMP}`: The temp directory.
* `{INPUT_PATH}`: The directory part of the current input, i.e., `/some/where` of input `/some/where/file.txt`.
* `{INPUT_NAMEEXT}`: The name (incl extension) of the current input, i.e., `file.txt` of input `/some/where/file.txt`.
* `{INPUT_NAMENOEXT}`: The name (excl extension) of the current input, i.e., `file` of input `/some/where/file.txt`.
* `{INPUT_EXT}`: The extension of the current input (incl dot), i.e., `.txt` of input `/some/where/file.txt`.
* `{INPUT_PARENT_PATH}`: The directory part of the parent directory of the current input, i.e., `/some` of input `/some/where/file.txt`.
* `{INPUT_PARENT_NAME}`: The name of the parent directory of the current input, i.e., `where` of input `/some/where/file.txt`.
