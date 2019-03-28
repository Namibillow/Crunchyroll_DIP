import random
import skimage as sk
from scipy import ndarray, ndimage
from skimage import io
import numpy as np
import os
from skimage.transform import AffineTransform, warp


def random_shift(img):
    vector = random.uniform(-10, 10), random.uniform(-10, 10)
    transform = AffineTransform(translation=vector)
    shifted = warp(img, transform, mode='wrap', preserve_range=True)

    return shifted.astype(img.dtype)


def random_noise(img):
    return sk.util.random_noise(img)


def rescale_intensity(img):
    v_min, v_max = np.percentile(img, (0.2, 99.8))
    return sk.exposure.rescale_intensity(img, in_range=(v_min, v_max))


transformation_order = {
    "noise": random_noise,
    "noise1": random_noise,
    "noise2": random_noise,
    "noise3": random_noise,
    "shift": random_shift,
    "rescale": rescale_intensity,
    "rescale1": rescale_intensity,
    "rescale2": rescale_intensity,
    "rescale3": rescale_intensity,
    "rescale4": rescale_intensity
}


def data_augment(source_directory=None, specific_dir=None):

    for root, dirs, files in os.walk(source_directory):

        # counter
        i = 1
        if not dirs and files is not None:  # if there is no sub dirs
            try:  # create a new directory per frame set
                save_path = root + '-copy' + str(i)
                print(save_path)
                os.mkdir(save_path)
            except OSError:
                print("Creation of the directory %s failed" % save_path)
            else:
                print("Successfully created the directory %s " % save_path)

        for name in files:
            print("root:, {} \n dir: {}. \n filename: {} \n".format(root, dirs, name))
            j = 1
            if name.endswith(".jpg"):
                # read image as an two dimensional array of pixels
                image_to_transform = io.imread(root + '/' + name)

                for k, v in transformation_order.items():
                    # perform augmentation
                    new_img = v(image_to_transform)
                    new_img_name = save_path + '/' + 'c' + str(j) + '.jpg'
                    # print(new_img_name)
                    io.imsave(new_img_name, new_img)
                    j += 1
        i += 1


'''
Pipeline(source_directory=storage+'Frames/', output_directory=storage+'Frames')
'''

'''
map look up for international morse code
json file
label should be 41 each hot encoded

{0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z', 26: '0', 27: '1', 28: '2', 29: '3', 30: '4', 31: '5', 32: '6', 33: '7', 34: '8', 35: '9', 36: '.',37: ',', 38: '?',39:'/', 40: '@'}
'''
dir = os.getcwd() + '/Dataset/PN/Frames/'
data_augment(source_directory=dir, specific_dir=None)
