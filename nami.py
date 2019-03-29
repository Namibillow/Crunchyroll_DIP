import random
import skimage as sk
from skimage import io
import numpy as np
import os
from skimage.transform import AffineTransform, warp
# from skimage.filters import gaussian


def random_shift(img):
    vector = random.uniform(-20, -40), random.uniform(-20, -40)
    transform = AffineTransform(translation=vector)
    shifted = warp(img, transform, mode='wrap', preserve_range=True)

    return shifted.astype(img.dtype)


def random_noise(img):
    variance = np.random.uniform(0., 0.1, 1)
    return sk.util.random_noise(img, mode="gaussian", var=variance)


def rescale_intensity(img):
    v_min, v_max = np.percentile(img, (0.5, 99.5))
    return sk.exposure.rescale_intensity(img, in_range=(v_min, v_max))


def random_blur(img):
    sig = random.uniform(0.5, 1.5)
    return rescale_intensity(sk.filters.gaussian(img, sigma=sig, multichannel=True))


transformation_order = {
    "blur": random_blur,
    "blur2": random_blur,
    "noise": random_noise,
    "noise1": random_noise,
    "noise2": random_noise,
    "shift": random_shift,
    "shift2": random_shift,
    "rescale": rescale_intensity,
    "rescale2": rescale_intensity
}


def data_augment(source_directory=None):
    '''
    args:
        source_directory - folder path you want to perform data augmentation

    return:
        None - folder is created for

    '''
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


#  Example: ###############################
# dir = os.getcwd() + '/Dataset/PN/Frames/'
# data_augment(source_directory=dir)
#########################################
