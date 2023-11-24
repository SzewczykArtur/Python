"""
This class is responsible for divided a photo for a colors. It's use two library PIL to open photo, and numpy, which
help save photo in numerical data.
"""
from PIL import Image
import numpy as np


class ImageColor:

    def __init__(self, img_path, delta):
        self.img_path = img_path
        self.delta = delta

    def color_dict(self):
        # Upload photo, and save it on numerical tabel
        photo = Image.open(self.img_path)
        img = np.array(photo)

        # Set how many colors can be. '//' perform integer division
        img = (img//self.delta)*self.delta
        new_img = np.array(img)

        # Get a points list of pixels, where every one point is saves as RGB code
        pixels = new_img.reshape((-1, 3))

        # Get unique colors and counts how many there are
        unique, counts = np.unique(pixels, axis=0, return_counts=True)

        # Total unique colors
        total = len(unique)
        dict_colors = {}
        sum_fo_color = 0
        # This loop is iterate as many different color as there are. Next it's add to dictionary like: "
        # '120, 120, 120': 100", 100 manes how many this color is on the picture
        for i in range(total):
            color = (unique[i][0], unique[i][1], unique[i][2])
            dict_colors[color] = counts[i]
            sum_fo_color += counts[i]
        # reverse sort dictionary from large number of colors to less
        sorted_dict = {k: v for k, v in sorted(dict_colors.items(), key=lambda item: item[1], reverse=True)}
        return sorted_dict

    def sum_of_colors(self):
        color_sum = 0
        color_dict = self.color_dict()
        for k, v in color_dict.items():
            color_sum += v
        return color_sum



