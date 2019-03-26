import random
import skimage as sk
from skimage import transform
from scipy import ndarray, ndimage
import numpy as np
import os


class Pipeline():
    def __init__(self, source_directory=None, output_directory=None, specific_dir=None):

        for root, dirs, files in os.walk(dir):
            for name in files:
                i = 1
                if name.endswith(".jpg"):
                    # perform augmentation
                    self.random_shift(name)

                    self.random_shift(name)

                    self.random_shit(name)

                    self.random_shift(name)

                    self.flip_horizontally(name)

                    self.random_noise(name)

                    self.random_rotation(name)

                    self.random_rotation(name)

                    self.rescale_intensity(name)

                    name = "copy" + str(i) + name
                    i += 1

    def random_shift(img):
        pass

    def random_noise(img):
        return sk.util.random_noise(img)

    def flip_horizontally(img):
        return img[:, ::-1]

    def random_rotation(img):
        random_degree = random.uniform(-15, 15)
        return sk.transform.rotate(img, random_degree)

    def rescale_intensity(img):
        v_min, v_max = np.percentile(img, (0.2, 99.8))
        return sk.exposure.rescale_intensity(img, in_range=(v_min, v_max))


'''
Pipeline(source_directory=storage+'Frames/', output_directory=storage+'Frames')
'''
