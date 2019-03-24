import cv2
import time
import uuid
import os

# Records video into [filepath]
def RecordVideo(filename, filepath):
    cap = cv2.VideoCapture(0)
    _key_name = uuid.uuid4()
    _path = '%s%s.mp4' % (filepath, filename + ' - ' + str(_key_name))

    # Define codec and create VideoWriter object.
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(_path, fourcc, 20.0, (640, 480))

    # Get frame dimmensions.
    width = int(cap.get(3))
    height = int(cap.get(4))

    _textLoc = (20, height - 10)  # Location where string will be overlayed.
    _startTime = time.time()

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            # Overlay timer string on frame.
            timer = time.time() - _startTime
            timerString = 'Recording for: %ds' % timer
            cv2.putText(frame, timerString, _textLoc, 1, 1, (0, 0, 255))

            # Write frame to file, then show it.
            out.write(frame)
            cv2.imshow(filename, frame)

            # Close video on 'Esc'.
            if cv2.waitKey(20) == 27:
                break
        else:
            break

    # Close everything >:(
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    os.mkdir(filepath + 'Frames/' + str(_key_name))
    SplitVideo(_path, filepath + 'Frames/' + str(_key_name))


# Splits video feed into individual frames and stores locally.


def SplitVideo(video, dest):
    cap = cv2.VideoCapture(video)
    success, image = cap.read()
    count = 0
    while success:
        cv2.imwrite('%s/frame%d.jpg' % (dest, count), image)
        success, image = cap.read()
        count += 1

    cap.release()
