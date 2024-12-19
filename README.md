# image-dataset-converter-paddle
[image-dataset-converter](https://github.com/waikato-datamining/image-dataset-converter) 
plugins for [Paddle (PArallel Distributed Deep LEarning)](https://github.com/PaddlePaddle).


## Installation

Via PyPI:

```bash
pip install image-dataset-converter-paddle
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


## Plugins

See [here](plugins/README.md) for an overview of all plugins.

