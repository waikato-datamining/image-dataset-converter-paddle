# from-paddle-is

* generates: idc.api.ImageSegmentationData

Loads the image segmentation from the specified text files listing image (JPG with relative path) and annotation image (indexed PNG with relative path). The labels (incl background) are specified via a separate text file.

```
usage: from-paddle-is [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                      [-N LOGGER_NAME] [-i [INPUT ...]] [-I [INPUT_LIST ...]]
                      [--labels_file FILE] [--labels [LABEL ...]]

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
                        supported (default: None)
  -I [INPUT_LIST ...], --input_list [INPUT_LIST ...]
                        Path to the text file(s) listing the text files to use
                        (default: None)
  --labels_file FILE    The file with the labels associated with the indices
                        (incl. background) (default: None)
  --labels [LABEL ...]  The labels that the indices represent (incl
                        background). (default: None)
```
