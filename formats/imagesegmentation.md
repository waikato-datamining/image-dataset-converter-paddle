# Image segmentation

The format uses a simple text file based approach with two files:
* labels list
* file list

## Labels list

The format is as follows:

```
background
label1
label2
label3
...
```
Each index from the indexed PNG annotations (starting with 0) must be listed.


## File list

The format is as follows:

```
img/0001.jpg ann/0001.png
img/0002.jpg ann/0002.png
img/0003.jpg ann/0003.png
...
```

Each line consists of the **relative image file name** and the associated 
**relative annotation image file name** separated by a blank.
