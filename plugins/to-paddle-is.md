# to-paddle-is

* accepts: idc.api.ImageSegmentationData

Saves the image segmentation in the specified text files listing image (with relative path) and annotation (with relative path). The labels get stored in a separate text file (one per line). When splitting, the split names get appended to the '--files' name (before the extension) separated by '-'.

```
usage: to-paddle-is [-h] [-l {DEBUG,INFO,WARNING,ERROR,CRITICAL}]
                    [-N LOGGER_NAME] [-r SPLIT_RATIOS [SPLIT_RATIOS ...]]
                    [-n SPLIT_NAMES [SPLIT_NAMES ...]] -o OUTPUT [-f NAME]
                    [-i PATH] [-a PATH] [-p PALETTE] [--labels NAME]
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
  -r SPLIT_RATIOS [SPLIT_RATIOS ...], --split_ratios SPLIT_RATIOS [SPLIT_RATIOS ...]
                        The split ratios to use for generating the splits
                        (must sum up to 100) (default: None)
  -n SPLIT_NAMES [SPLIT_NAMES ...], --split_names SPLIT_NAMES [SPLIT_NAMES ...]
                        The split names to use for the generated splits.
                        (default: None)
  -o OUTPUT, --output OUTPUT
                        The directory to store the data in. Any defined splits
                        get added beneath there. (default: None)
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
  --annotations_only    Outputs only the annotations and skips the base image.
                        (default: False)
```
