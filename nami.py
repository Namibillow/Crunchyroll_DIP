import imgaug as ia
import numpy as np
import os
from imgaug import augmenters as iaa
# import imageio as io
from skimage import io

# defining our sequence of augmentation we want to apply
augmenters = [
    iaa.GaussianBlur(sigma=(1.0, 3.0)),  # blur images with a sigma of 0 to 2.0
    iaa.MotionBlur((3, 5)),  # blur image
    iaa.AdditiveGaussianNoise(scale=(0, 0.05 * 255)),  # Add gaussian noise to an image, sampled once per pixel from a normal distribution N(0, 0.05*255)
    iaa.AdditiveLaplaceNoise(scale=(0, 0.05 * 255)),
    iaa.Multiply((0.5, 1.5), per_channel=0.5),
    iaa.Multiply((0.5, 1.5)),  # Multiply each image with a random value between 0.5 and 1.5:

    iaa.Dropout(p=(0.05, 0.15)),  # Sample per image a value p from the range 0.05<=p<=0.15 and then drop p percent of all pixels in the image (i.e. convert them to black pixels):

    iaa.ImpulseNoise(p=(0.03, 0.06)),
    iaa.Salt(p=(0.03, 0.05)),
    iaa.Add((-30, 30)),  # adding random value to pixels
    iaa.SigmoidContrast(6.1, 0.5),
    iaa.PerspectiveTransform(scale=0.02),
    iaa.PerspectiveTransform(scale=0.01),
    iaa.PerspectiveTransform(scale=0.015),
    iaa.PerspectiveTransform(scale=0.03),
    iaa.PiecewiseAffine(scale=0.02),
    iaa.PiecewiseAffine(scale=0.03),
    iaa.PiecewiseAffine(scale=0.01),
    iaa.Crop(px=(10, 20), keep_size=True),
    iaa.Crop(px=(20, 35))
]


def check_dir_or_create(dir):
    '''
    create a directory to store generated images. If dir is already exists, then it will ask you to name the new directory
    '''
    if os.path.exists(dir):
        new_dir = input('Type different directory name (no slashes needed): \n')
        first_part, _ = os.path.split(dir)

        # only change the last directory Name
        dir = os.path.join(first_part, new_dir)

    os.makedirs(dir)
    print(f"successfully made new directory: {dir}")


def apply_aug(f, image):
    '''
    input:
        f : augment function that will be applied
        image : an image
    return:
        tranformed_image
    '''
    return f.augment_image(image)


def get_immediate_subdirectories(p_dir):
    '''
    input:
        p_dir: parent directory
    return:
        list of immediate subdirectories of p_dir
    '''
    return [name for name in os.listdir(p_dir)
            if os.path.isdir(os.path.join(p_dir, name))]


def get_image_files(p_dir):
    '''
    input:
        p_dir: parent directory
    return:
        list of all image files in p_dir
    '''
    # change img.endswith input parameter for different images.
    return [img for img in os.listdir(p_dir) if img.endswith('jpg')]


def load_img(image_path):
    '''
    Input:
        image_path: absolute path of where image is at
    Output:
        numpy array of the image
    '''
    return io.imread(image_path)


def perform_aug(images, path):
    img_pathes = [os.path.join(path, image) for image in images]
    print(img_pathes)  # eg. ['/test1/test2/test3/dog4.jpg',...]
    c = 0
    for aug in augmenters:
        # turn to list of absolute pathes of images
        aug_images = [apply_aug(aug, load_img(im_path)) for im_path in img_pathes]
        print(f'num of aug_images should be {len(img_pathes)} and actually {len(aug_images)}')
        # get the directory name of this file
        dir_name = os.path.basename(os.path.dirname(img_pathes[0]))  # 'test3'
        dir_path = os.path.dirname(img_pathes[0])  # '/test1/test2/test3'

        # create new directory
        new_dir_path = dir_path.replace(dir_name, dir_name + '_c_' + str(c + 1), 1)  # '/test1/test2/test3_c_1'
        check_dir_or_create(new_dir_path)

        i = 0
        for im in aug_images:

            orig_im_name = os.path.basename(img_pathes[i])  # 'dog4.jpg'

            # uncomment following this if you change the image names #
            # orig_filename, ext = os.path.splitext(orig_im_name)  # ['dog4','.jpg']

            # new_filename = orig_filename + '_copy_{}'.format(c + 1) + ext  # 'dog4_copy_1.jpg'

            # concatinate new directory and new image name
            new_path = os.path.join(new_dir_path, orig_im_name)

            # save image
            io.imsave(new_path, im)
            i += 1
        c += 1

    print('aug done!')


def data_augment(dir):
    # if dir is a directory and the directory is not empty
    if os.path.isdir(dir) and not len(os.listdir(dir)) == 0:

        # Check if there are subdirectories
        folders = get_immediate_subdirectories(dir)
        print(f"There are total of : {len(folders)}")
        print("Folders are: ", folders)

        # if you passed parent folder containing multiple subfolders
        if folders:
            for folder in folders:
                fullPath = os.path.join(dir, folder)
                images = get_image_files(fullPath)

                print(f'folder "{folder}" has {len(images)} pictures.')
                print('images: ', images)

                # If there are any images, then apply augmentation
                if images:
                    perform_aug(images, fullPath)

        #  if there is no subfolders, but files, then just get all images
        else:
            images = get_image_files(dir)
            if images:
                perform_aug(images, dir)

    # if dir is just an image file
    elif os.path.isfile(dir) and dir.endswith(".jpg"):
        seq = iaa.Sequential(augmenters, random_order=False)
        image = load_img(dir)
        images_aug = seq.augment_image(image)
        # save augmented images in same directory
        for im in images_aug:
            # counter
            c = 1
            root, ext = os.path.splitext(dir)
            new_path = root + '_copy_{}'.format(c) + ext
            # ex: if original image is frog.jpg then new image will be named as frog_copy_1.jpg
            c += 1
            io.imsave(new_path, im)
    else:
        print("You passed non existing thing...")
    return


if __name__ == "__main__":
    ################ Example calling ###############################
    source_path = os.getcwd() + '/Dataset/toy/'

    #source_path = os.getcwd()
    data_augment(dir=source_path)
