# from-paddle-ic

* generates: idc.api.ImageClassificationData

Loads the image classification from the specified text files listing image (with relative path) and the associate label ID. The label ID to text mapping can be supplied as separate text file (ID <space> text).

```
usage: from-paddle-ic [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                      [-N LOGGER_NAME] [-i [INPUT ...]] [-I [INPUT_LIST ...]]
                      [-m FILE]

Loads the image classification from the specified text files listing image
(with relative path) and the associate label ID. The label ID to text mapping
can be supplied as separate text file (ID <space> text).

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
  -m FILE, --id_label_map FILE
                        The mapping between label ID and text (ID <space>
                        text); Supported placeholders: {HOME}, {CWD}, {TMP}
                        (default: None)
```

Available placeholders:

* `{HOME}`: The home directory of the current user.
* `{CWD}`: The current working directory.
* `{TMP}`: The temp directory.
