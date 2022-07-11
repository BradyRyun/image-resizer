# Image Resizer

### Requirements
* Python

### Dependencies
* Pillow \
`pip install Pillow`
  
### Usage
```
$ python main.py --help
usage: main.py [-h] --path PATH --height HEIGHT --width WIDTH [--recursive RECURSIVE]
               [--sampler {LANCZOS,HAMMING,BICUBIC,BILINEAR,BOX,NEAREST}]

optional arguments:
  -h, --help            show this help message and exit
  --path PATH           Path to get files from
  --height HEIGHT       Height to resize files to.
  --width WIDTH         Width to resize files to.
  --recursive           Use if the path specified should recursively update all nested directories.
  --sampler {LANCZOS,HAMMING,BICUBIC,BILINEAR,BOX,NEAREST}
                        Specify a specific resampler. Default: LANCZOS

```

### Single file

```bash
$ python main.py --path /path/to/image.png --height 64 --width 64
```

### Single directory
```bash
$ python main.py --path /path/to/dir --height 64 --width 64
```

#### Top-level Usage
```
# Beginning:
└───dir
    ├───dir3
        └───image.png
    └───dir4
        └───image.png
```
``` bash
$ python main.py --path /path/to/dir --height 64 --width 64 --recursive True

└───dir
    ├───dir3
        └───image.png
        └───image-64x64.png
    └───dir4
        └───image.png
        └───image-64x64.png
```