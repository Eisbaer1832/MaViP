import cv2

breaks = [1, 1.5, 2]

cv2.namedWindow("Name");
cv2.setWindowProperty("Name",cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN);
cap = cv2.VideoCapture('video.mp4')

if (cap.isOpened()== False):
    print("Error opening video file")


# used for second calculation
fps = cap.get(cv2.CAP_PROP_FPS)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        second = int(cap.get(cv2.CAP_PROP_POS_FRAMES))/fps
        cv2.imshow('Name', frame)
        
        if second in breaks:
            cv2.waitKey()

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()


