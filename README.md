# image-dataset-converter-paddle
[image-dataset-converter](https://github.com/waikato-datamining/image-dataset-converter) 
plugins for [Paddle (PArallel Distributed Deep LEarning)](https://github.com/PaddlePaddle).


## Installation

Via PyPI:

```bash
pip install image_dataset_converter_paddle
```

The latest code straight from the repository:

```bash
pip install git+https://github.com/waikato-datamining/image-dataset-converter-paddle.git
```

## Dataset formats

The following dataset formats are supported:

| Domain               | Format                                   | Read                           | Write                        | 
|:---------------------|:-----------------------------------------|:-------------------------------|:-----------------------------| 
| Image classification | [Paddle](formats/imageclassification.md) | [Y](plugins/from-paddle-ic.md) | [Y](plugins/to-paddle-ic.md) | 
| Image segmentation   | [Paddle](formats/imagesegmentation.md)   | [Y](plugins/from-paddle-is.md) | [Y](plugins/to-paddle-is.md) | 


## Tools

### VisualDL information

```
usage: idc-visualdl-info [-h] --log_file LOG_FILE [-i {tags,data}]
                         [-c COMPONENT] [-t TAG] [-o OUTPUT]
                         [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]

Tool for outputting information on VisualDL log files.

options:
  -h, --help            show this help message and exit
  --log_file LOG_FILE   The log file to read; Supported placeholders: {HOME},
                        {CWD}, {TMP}, {INPUT_PATH}, {INPUT_NAMEEXT},
                        {INPUT_NAMENOEXT}, {INPUT_EXT}, {INPUT_PARENT_PATH},
                        {INPUT_PARENT_NAME} (default: None)
  -i {tags,data}, --info_type {tags,data}
                        The type of information to generate. (default: tags)
  -c COMPONENT, --component COMPONENT
                        The component for which to output the data, e.g.,
                        'scalar'. (default: None)
  -t TAG, --tag TAG     The tag for which to output the data, e.g.,
                        'Evaluate/mIoU'. (default: None)
  -o OUTPUT, --output OUTPUT
                        The file to store the information in rather than
                        outputting it on stdout. (default: None)
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
```


## Plugins

See [here](plugins/README.md) for an overview of all plugins.
