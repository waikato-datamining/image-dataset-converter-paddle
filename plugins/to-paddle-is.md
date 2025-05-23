# to-paddle-is

* accepts: idc.api.ImageSegmentationData

Saves the image segmentation in the specified text files listing image (with relative path) and annotation (with relative path). The labels get stored in a separate text file (one per line). When splitting, the split names get appended to the '--files' name (before the extension) separated by '-'.

```
usage: to-paddle-is [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                    [-N LOGGER_NAME] [--skip]
                    [--split_ratios SPLIT_RATIOS [SPLIT_RATIOS ...]]
                    [--split_names SPLIT_NAMES [SPLIT_NAMES ...]]
                    [--split_group SPLIT_GROUP] -o OUTPUT [-f NAME] [-i PATH]
                    [-a PATH] [-p PALETTE] [--labels NAME] [--separator SEP]
                    [--annotations_only]

Saves the image segmentation in the specified text files listing image (with
relative path) and annotation (with relative path). The labels get stored in a
separate text file (one per line). When splitting, the split names get
appended to the '--files' name (before the extension) separated by '-'.

options:
  -h, --help            show this help message and exit
  -l {DEBUG,INFO,WARNING,ERROR,CRITICAL}, --logging_level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                        The logging level to use. (default: WARN)
  -N LOGGER_NAME, --logger_name LOGGER_NAME
                        The custom name to use for the logger, uses the plugin
                        name by default (default: None)
  --skip                Disables the plugin, removing it from the pipeline.
                        (default: False)
  --split_ratios SPLIT_RATIOS [SPLIT_RATIOS ...]
                        The split ratios to use for generating the splits
                        (must sum up to 100) (default: None)
  --split_names SPLIT_NAMES [SPLIT_NAMES ...]
                        The split names to use for the generated splits.
                        (default: None)
  --split_group SPLIT_GROUP
                        The regular expression with a single group used for
                        keeping items in the same split, e.g., for identifying
                        the base name of a file or the sample ID. (default:
                        None)
  -o OUTPUT, --output OUTPUT
                        The directory to store the data in. Any defined splits
                        get added beneath there. Supported placeholders:
                        {INPUT_PATH}, {INPUT_NAMEEXT}, {INPUT_NAMENOEXT},
                        {INPUT_EXT}, {INPUT_PARENT_PATH}, {INPUT_PARENT_NAME}
                        (default: None)
  -f NAME, --files NAME
                        The text file to store the relation of images with
                        their label indices in, e.g., 'data.txt' (default:
                        data.txt)
  -i PATH, --img_relative_path PATH
                        The relative path to store the images under, e.g.,
                        'img' (default: img)
  -a PATH, --ann_relative_path PATH
                        The relative path to store the annotations under,
                        e.g., 'ann' (default: ann)
  -p PALETTE, --palette PALETTE
                        The palette to use; either palette name (auto|colorbli
                        nd12|colorblind15|colorblind24|colorblind8|dark|graysc
                        ale|light|x11) or comma-separated list of R,G,B
                        values. (default: auto)
  --labels NAME         The name of the labels text file (no path), e.g.,
                        'labels.txt'. (default: labels.txt)
  --separator SEP       The separator to use for reading the text files.
                        (default: )
  --annotations_only    Outputs only the annotations and skips the base image.
                        (default: False)
```

Available placeholders:

* `{INPUT_PATH}`: The directory part of the current input, i.e., `/some/where` of input `/some/where/file.txt`.
* `{INPUT_NAMEEXT}`: The name (incl extension) of the current input, i.e., `file.txt` of input `/some/where/file.txt`.
* `{INPUT_NAMENOEXT}`: The name (excl extension) of the current input, i.e., `file` of input `/some/where/file.txt`.
* `{INPUT_EXT}`: The extension of the current input (incl dot), i.e., `.txt` of input `/some/where/file.txt`.
* `{INPUT_PARENT_PATH}`: The directory part of the parent directory of the current input, i.e., `/some` of input `/some/where/file.txt`.
* `{INPUT_PARENT_NAME}`: The name of the parent directory of the current input, i.e., `where` of input `/some/where/file.txt`.
