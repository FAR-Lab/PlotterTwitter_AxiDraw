import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

# def video_to_frames(vid_path, start_second, end_second):
#     """
#     Load a video and return its frames from the wanted time range.
#     :param vid_path: video file path.
#     :param start_second: time of first frame to be taken from the
#     video in seconds.
#     :param end_second: time of last frame to be taken from the
#     video in seconds.
#     :return:
#     frame_set: a 4D uint8 np array of size [num_of_frames x H x W x C]
#     containing the wanted video frames in BGR format.
#     """
#     cap = cv.VideoCapture(vid_path)
#     if not cap.isOpened():
#         print("Cannot open video")
#         exit()
#
#     # Get the frame rate of the video
#     fps = cap.get(cv.CAP_PROP_FPS)
#
#     # Calculate the time of the first frame
#     start_time = start_second * fps
#
#     # Calculate the time of the last frame
#     end_time = end_second * fps
#
#     # Calculate the number of frames to be taken
#     num_of_frames = int(end_time - start_time)
#     # Create an empty array to store the frames
#     frame_set = np.empty((num_of_frames, *cap.read()[1].shape), dtype=np.uint8)
#
#     # Read the frames from the video
#     for f in range(num_of_frames):
#         cap.set(cv.CAP_PROP_POS_FRAMES, start_time + f)
#         frame_set[f] = cap.read()[1]
#     return frame_set

if __name__ == '__main__':
    cap = cv.VideoCapture(1)
    if not cap.isOpened():
         print("Cannot open camera")
         exit()
    while True:
    # Capture frame-by-frame
        ret, frame = cap.read()
     # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
         # Our operations on the frame come here
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
     # Display the resulting frame
        cv.imshow('frame', gray)
        if cv.waitKey(1) == ord('q'):
            break
        # When everything done, release the capture
        cap.release()
    # cv.destroyAllWindows()

