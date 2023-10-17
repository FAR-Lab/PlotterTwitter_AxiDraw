import cv2
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv



if __name__ == '__main__':
    # Create a work space Camera object
    cap = cv.VideoCapture(2)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    # image_path = r'C:\Users\97250\PycharmProjects\pythonProject4\IMG_4902.JPG'
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        # Display the resulting frame
        cv.imshow('frame', gray)
        if cv.waitKey(1) == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv.imshow()

