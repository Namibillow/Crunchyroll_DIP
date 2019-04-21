import os
import cv2

# Splits video feed into individual frames and stores locally.
def SplitVideo(video: str, dest: str):
    cap = cv2.VideoCapture(video)
    success, image = cap.read()
    count = 0
    while success:
        cv2.imwrite('%s/frame%d.jpg' % (dest, count), image)
        success, image = cap.read()
        count += 1

    cap.release()


def create_folder(video_name, dest_path):
    '''
    Return the label dir for that video
    '''
    root, ext = os.path.splitext(video_name) #dot1
    print(root)
    print(dest_path)
    label_path = os.path.join(dest_path, root)
    try:
        os.mkdir(label_path)
    except:
        print("Oops!", label_path, "doesnt exist\n")
   

    return label_path



def build_dataset(videos, dest_path):
    for video in videos:
        label_path = create_folder(video, dest_path)
        SplitVideo(video=video, dest=label_path)


# def create_dir(train_p, test_p):
#     for path in [train_p, test_p]:
#         for i in range(21):
#             os.mkdir(os.path.join(path, 'digit_' + str(i)))


if __name__ == "__main__":
    parent_dir = os.path.join(os.getcwd(),'Dataset/PD/RawData')
    #print(parent_dir)

    videos = os.listdir(parent_dir)
    videos = [os.path.join(parent_dir, v) for v in videos if v.endswith('avi')]

    # print(videos)

    # Split the videos to train and test
    # test_size = len(videos) * 0.2

    # train = videos[test_size:]
    # test = videos[:test_size]

    train_dest = 'Dataset/train'
    #print(train_dest)
    # test_dest = os.path.join(os.getcwd(), 'Dataset/test')

    # create_dir(train_dest,test_dest)

    build_dataset(videos, train_dest)
    # build_dataset(test, test_dest)


'''


Datasets/
Train/
    p1_dot/
        frame1.jpg
        Frame2
    p1_dash/
    p2_dot/
    p2_dash/


Test/

'''
