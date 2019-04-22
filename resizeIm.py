import os
import cv2

# Resizes images in ./Dataset/train/[dir]... directory.
os.chdir(os.path.abspath('./Dataset/train/'))
for im_dir in os.walk('.'):
    for im in im_dir[2]:
        tmp = im_dir[0].replace('.', '')
        absPath = os.getcwd()+tmp+'\\'+im
        image = cv2.imread(absPath)
        h,w,d = image.shape

        newX, newY = image.shape[1]*imgScale, image.shape[0]*imgScale
        newimg = cv2.resize(image, (100, 100))
        cv2.imshow('resized', newimg)
        cv2.waitKey(0)


