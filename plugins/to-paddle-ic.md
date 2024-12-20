# to-paddle-ic

* accepts: idc.api.ImageClassificationData

Saves the image classification in the specified text files listing image (with relative path) and the associate label ID. The label ID to text mapping is stored in a separate text file (ID <space> text).

```
usage: to-paddle-ic [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                    [-N LOGGER_NAME] [-r SPLIT_RATIOS [SPLIT_RATIOS ...]]
                    [-n SPLIT_NAMES [SPLIT_NAMES ...]] -o OUTPUT [-f NAME]
                    [-p PATH] [-m NAME] [--annotations_only]

Saves the image classification in the specified text files listing image (with
relative path) and the associate label ID. The label ID to text mapping is
stored in a separate text file (ID <space> text).

options:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
  -N LOGGER_NAME, --logger_name LOGGER_NAME
                        The custom name to use for the logger, uses the plugin
                        name by default (default: None)
  -r SPLIT_RATIOS [SPLIT_RATIOS ...], --split_ratios SPLIT_RATIOS [SPLIT_RATIOS ...]
                        The split ratios to use for generating the splits
                        (must sum up to 100) (default: None)
  -n SPLIT_NAMES [SPLIT_NAMES ...], --split_names SPLIT_NAMES [SPLIT_NAMES ...]
                        The split names to use for the generated splits.
                        (default: None)
  -o OUTPUT, --output OUTPUT
                        The directory to store the data in. Any defined splits
                        get added beneath there. (default: None)
  -f NAME, --file_label_map NAME
                        The text file to store the relation of images with
                        their label indices in, e.g., 'annotations.txt'
                        (default: annotations.txt)
  -p PATH, --relative_path PATH
                        The relative path to the annotations text file to
                        store the images under, e.g., 'images' (default:
                        images)
  -m NAME, --id_label_map NAME
                        The name of the ID/label text mapping text file (no
                        path), e.g., 'labels.map'. (default: labels.map)
  --annotations_only    Outputs only the annotations and skips the base image.
                        (default: False)
```
