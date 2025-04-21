import cv2
import numpy as np
breaks = []
lastframe = ""
laststopped = ""
cv2.namedWindow("Name");
cv2.setWindowProperty("Name",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN);
cap = cv2.VideoCapture('video.mp4')

def is_similar(image1, image2):
    difference = cv2.absdiff(image1, image2)
    max_diff = np.max(difference)
    if max_diff <= 2: # allow tollerance of 2px, which may occur due to compression
        return True
    else:
        return False

if (cap.isOpened()== False):
    print("Error opening video file")


# used for second calculation
fps = cap.get(cv2.CAP_PROP_FPS)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        second = int(cap.get(cv2.CAP_PROP_POS_FRAMES))/fps
        cv2.imshow('Name', frame)

        if int(cap.get(cv2.CAP_PROP_POS_FRAMES)) > 1:
            if is_similar(frame, lastframe) and not is_similar(frame,laststopped):
                laststopped = frame
                key = cv2.waitKey(0)
        else:
            laststopped = frame
        lastframe = frame.copy()

        if second in breaks:
            cv2.waitKey()

        key = cv2.waitKey(25) & 0xFF 
        if key == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

