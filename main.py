import argparse
from resizer import Resizer

if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--path",
                      help="Path to get files from",
                      required=True,
                      type=str)
    args.add_argument("--height",
                      help="Height to resize files to.",
                      required=True,
                      type=int)
    args.add_argument("--width",
                      help="Width to resize files to.",
                      required=True,
                      type=int)
    args.add_argument("--recursive",
                      help="Use if the path specified should recursively update all nested directories.",
                      required=False,
                      action="store_true")
    args.add_argument("--sampler", help="Specify a specific resampler. Default: LANCZOS",
                      required=False,
                      default="LANCZOS",
                      choices=[
                          "LANCZOS",
                          "HAMMING",
                          "BICUBIC",
                          "BILINEAR",
                          "BOX",
                          "NEAREST"
                      ])
    args.add_argument("--remove",
                      help="Use if you'd like to remove the original image.",
                      required=False,
                      action="store_true")

    parsed = args.parse_args()
    p = parsed.path
    h = parsed.height
    w = parsed.width
    s = parsed.sampler
    r = parsed.recursive
    rm = parsed.remove

    resizer = Resizer(height=h, width=w, sampler=s, remove_old=rm)

    if resizer.is_image(p):
        file = p.split('/')[-1]
        d = "/".join(p.split('/')[:-1])
        resizer.resize(d, file)
    if r:
        resizer.recursively_resize(p)
    else:
        files = resizer.resize_images(p)