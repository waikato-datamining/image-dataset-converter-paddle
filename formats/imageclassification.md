# Image classification

The format uses a simple text file based approach with two files:
* file/label index map
* label index/label text map

## File/label index map

The format is as follows:

```
path/image1.jpg 0
path/image2.jpg 1
path/image3.jpg 10
path/image4.jpg 2
...
```

Each line consists of the **relative image file name** and the associated **label index** separated by a blank.


## Label index/label text map

The format is as follows:

```
0 first label
1 second label
2 third label
...
```

Each line consists of the **label index** separated by a blank from the **label text**. 
