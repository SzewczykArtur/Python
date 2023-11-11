from PIL import Image
import numpy as np


class ImageColor:

    def __init__(self, img_path, delta):
        self.img_path = img_path
        self.delta = delta

    def color_dict(self):
        # Upload photo
        photo = Image.open(self.img_path)
        img = np.array(photo)

        # Set how many colors can be
        img = (img//self.delta)*self.delta
        new_img = np.array(img)

        # Get a list point of pixels
        pixels = new_img.reshape((-1, 3))

        # Get unique colors and counts how many there are
        unique, counts = np.unique(pixels, axis=0, return_counts=True)

        # Total unique colors
        total = len(unique)
        dict_colors = {}
        sum_fo_color = 0
        for i in range(total):
            color = (unique[i][0], unique[i][1], unique[i][2])
            dict_colors[color] = counts[i]
            sum_fo_color += counts[i]
        sorted_dict = {k: v for k, v in sorted(dict_colors.items(), key=lambda item: item[1], reverse=True)}
        return sorted_dict

    def sum_of_colors(self):
        color_sum = 0
        color_dict = self.color_dict()
        for k,v in color_dict.items():
            color_sum += v
        return color_sum

