import cv2
import time
import math

# Records video into [filepath]
def RecordVideo(filename, filepath):
    cap = cv2.VideoCapture(0)

    # Define codec and create VideoWriter object.
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(filepath, fourcc, 20.0, (640,480))

    # Get frame dimmensions.
    width = int(cap.get(3))
    height = int(cap.get(4))

    _textLoc = (20, height - 10)
    _startTime = time.time()

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            # Overlay timer string on frame. 
            timer = time.time() - _startTime
            timerString = 'Recording for: %ds' % timer
            cv2.putText(frame, timerString, _textLoc, 1, 1, (0,0,255))

            # Write frame to file, then show it.
            out.write(frame)
            cv2.imshow(filename, frame)

            # Close video on 'Esc'.
            if cv2.waitKey(20) == 27:
                break
        else: break
    
    # Close everything >:(
    cap.release()
    out.release()
    cv2.destroyAllWindows()
