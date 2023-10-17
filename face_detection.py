import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

# def find_center_of_face():


if __name__ == '__main__':
    # Create a work space Camera object
    cap = cv.VideoCapture(0)
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
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        img = cv.cvtColor(frame, cv.COLOR_BGRA2BGR)
        classifier = cv.CascadeClassifier(
            r'C:\Users\97250\PycharmProjects\pythonProject4\classifiers\haarcascade_frontalface_default.xml'
        )
        # classifier = cv.CascadeClassifier(
        #     r'C:\Users\97250\PycharmProjects\pythonProject4\classifiers\haarcascade_fullbody.xml'
        # )
        color = (0, 255, 0)
        faceRects = classifier.detectMultiScale(
            gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
        if len(faceRects):
            for faceRect in faceRects:
                x, y, w, h = faceRect
                cv.rectangle(img, (x, y), (x + h, y + w), color, 2)
                cv.circle(img, center=(x+w//2, y+h//2), radius=5, color=(0, 255, 0))
                # cv.circle(img, (x + w // 4, y + h // 4 + 30), min(w // 8, h // 8),
                #            color)
                #
                # cv.circle(img, (x + 3 * w // 4, y + h // 4 + 30), min(w // 8, h // 8),
                #            color)
                #
                # cv.rectangle(img, (x + 3 * w // 8, y + 3 * h // 4),
                #               (x + 5 * w // 8, y + 7 * h // 8), color)

        # Display the resulting frame
        cv.imshow('frame', img)
        if cv.waitKey(1) == ord('q'):
            break
    # When everything done, release the capture
    cap.release()
    cv.imshow()

