from os import path, walk, listdir
from PIL import Image


class Resizer:
    resizers = {
        "LANCZOS": Image.Resampling.LANCZOS,
        "HAMMING": Image.Resampling.HAMMING,
        "BICUBIC": Image.Resampling.BICUBIC,
        "BILINEAR": Image.Resampling.BILINEAR,
        "BOX": Image.Resampling.BOX,
        "NEAREST": Image.Resampling.NEAREST
    }

    def __init__(self, height, width, sampler):
        self.height = height
        self.width = width
        self.sampler = self.resizers[sampler]

    def is_image(self, file):
        return file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif'))

    def get_images_in_path(self, dir):
        images = [f for f in listdir(dir) if self.is_image(f)]
        return images

    def get_folders_in_dir(self, dir):
        dirs = [x[0] for x in walk(dir)]
        return dirs

    def resize_images(self, dirPath):
        files = self.get_images_in_path(dirPath)
        for file in files:
            self.resize(dirPath)

    def resize(self, directory, file):
        image = Image.open(path.join(directory, file))
        print(f"Current file: {file}\nCurrent size: {image.size}")  # 5464x3640
        split = file.split('.')
        name = split[0]
        extension = split[1]
        img_resized = image.resize((self.height, self.width), resample=self.sampler)
        img_resized.save(path.join(directory, f"{name}-{self.height}x{self.width}.{extension}"))

    def recursively_resize(self, dir):
        dirs = self.get_folders_in_dir(dir)
        for x in dirs:
            if x == dir:
                dirs.remove(x)
        if len(dirs) == 0:
            return
        for d in dirs:
            self.resize_images(d)
            self.recursively_resize(d)
