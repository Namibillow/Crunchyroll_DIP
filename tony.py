import cv2
import time
import uuid
import os
from math import floor

# Records video into [filepath]
def RecordVideo(filename, filepath):
    cap = cv2.VideoCapture(0)
    _key_name = uuid.uuid4()
    _path = '%s%s.avi' % (filepath, filename + '-' + str(_key_name)) # avi for windows.

    # Get the width and height of frame
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)

    # Define codec and create VideoWriter object.
    fourcc = cv2.VideoWriter_fourcc(*'XVID') # XVID for windows
    out = cv2.VideoWriter(_path, fourcc, 20.0, (width, height))

    _textLoc = (20, height - 10)  # Location where string will be overlayed.
    _startTime = time.time()

    # Location coordinates for rectangle overlay.
    (x1,y1) = floor(width/4), floor(height*2/10)
    (x2,y2) = floor((width*3)/4), floor((height*4)/10) 

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.flip(frame,180)

            # Overlay timer string on frame.
            timer = time.time() - _startTime
            timerString = 'Recording for: %ds' % timer
            cv2.putText(frame, timerString, _textLoc, 1, 1, (0, 0, 255))

            # Overlay rectangle for face & crop positioning.
            cv2.rectangle(
                frame, 
                (x1,y1), # top-left
                (x2,y2), # bottom-right
                (0,255,255), # color
                2) # thickness

            # Write frame to file, then show it.
            out.write(frame)
            cv2.imshow(filename, frame)

            # Close video on 'Esc'.
            if cv2.waitKey(20) == 27:
                break
        else:
            break

    # Close everything >:(
    out.release()
    cap.release()
    cv2.destroyAllWindows()

    os.mkdir(filepath + 'Frames/' + str(_key_name))
    SplitVideo(_path, filepath + 'Frames/' + str(_key_name), (x1,y1), (x2,y2))


# Splits video feed into individual frames and stores locally.
def SplitVideo(video: str, dest: str, p1: int, p2: int):
    cap = cv2.VideoCapture(video)
    success, image = cap.read()
    count = 0
    while success:
        # crop image with some offset to eliminate rectangle overlay.
        image = image[p1[1]+2:p2[1]-2, p1[0]+2:p2[0]-2]
        
        cv2.imwrite('%s/frame%d.jpg' % (dest, count), image)
        success, image = cap.read()
        count += 1

    cap.release()
