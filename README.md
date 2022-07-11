# Image Resizer

### Requirements
* Python

### Dependencies
* Pillow \
`pip install Pillow`
  
### Usage
``` bash
usage: main.py [-h] --path PATH --height HEIGHT --width WIDTH [--top-level TOP_LEVEL]

optional arguments:
  -h, --help            show this help message and exit
  --path PATH           Path to get files from
  --height HEIGHT       Height to resize files to.
  --width WIDTH         Width to resize files to.
  --top-level TOP_LEVEL
                        Use if the path specified should recursively update all nested directories.
```

### 

#### Top-level Usage
```angular2html
# Beginning:
└───dir
    ├───dir3
        └───image.png
    └───dir4
        └───image.png
```
```
$ python main.py --path ./dir --height 64 --width 64 --top-level True

└───dir
    ├───dir3
        └───image.png
        └───image-64x64.png
    └───dir4
        └───image.png
        └───image-64x64.png
```