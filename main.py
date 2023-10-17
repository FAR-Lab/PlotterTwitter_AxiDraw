import pixels2svg as pixels2svg
import svgtrace
from pyaxidraw import axidraw
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import aspose.words as aw
from PIL import Image as im
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM, renderSVG
import os
import potrace
import scipy as sp
import pyzed.sl as sl

def convert_to_svg(image):
    # convert to png
    image = image.astype(np.uint8)
    # resize
    width = 290
    height = 210
    dim = (width, height)
    image = cv.resize(image, dim, interpolation=cv.INTER_AREA)
    image = im.fromarray(image)
    image.save("Output.png", "PNG")
    #  Create document object
    image = svg2rlg(r'C:\Users\97250\PycharmProjects\pythonProject4\drawing.svg')
    doc = aw.Document()
    # Create a document builder object
    builder = aw.DocumentBuilder(doc)
    # Load and insert PNG image
    shape = builder.insert_image("Output.png")
    # Specify image save format as SVG
    saveOptions = aw.saving.ImageSaveOptions(aw.SaveFormat.SVG)
    # Save image as SVG
    shape.get_shape_renderer().save("Output.svg", saveOptions)
    # # shape.image_data.save("Output.svg")


def draw_image(svg_image):
    ad = axidraw.AxiDraw()  # Initialize class
    DXL_IDS = [1, 2]  # define motors ID
    M1 = axidraw.Motor(DXL_IDS)  # Initialize motors
    M1.Enable_Torque()
    try:
        M1.Homeing()
        ad.plot_setup(svg_image)
        ad.options.pen_pos_up = 70      # set pen-up position
        ad.plot_run()
    except:
        print("Cant plot the image")


if __name__ == '__main__':
    # Read images
    image_path = r'test.svg'
    # Create a zed Camera object
    # zed = sl.Camera()
    # # Create a InitParameters object and set configuration parameters
    # init_params = sl.InitParameters()
    # init_params.depth_mode = sl.DEPTH_MODE.PERFORMANCE
    # init_params.coordinate_units = sl.UNIT.METER
    # init_params.sdk_verbose = True
    # # Open the camera
    # err = zed.open(init_params)
    # if err != sl.ERROR_CODE.SUCCESS:
    #     exit(1)
    #
    # # Create a work space Camera object
    # cap = cv.VideoCapture(1)
    # if not cap.isOpened():
    #     print("Cannot open camera")
    #     exit()
    # # image_path = r'C:\Users\97250\PycharmProjects\pythonProject4\IMG_4902.JPG'
    # while True:
    #     # Capture frame-by-frame
    #     ret, frame = cap.read()
    #     # if frame is read correctly ret is True
    #     if not ret:
    #         print("Can't receive frame (stream end?). Exiting ...")
    #         break
    #         # Our operations on the frame come here
    #         gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #         # Display the resulting frame
    #         cv.imshow('frame', gray)
    #         if cv.waitKey(1) == ord('q'):
    #             break
    # # When everything done, release the capture
    # cap.release()
    # cv.imshow()
    img_gray = cv.imread(image_path, cv.IMREAD_GRAYSCALE)
    assert img_gray is not None, "file could not be read, check with os.path.exists()"
    img_blur = cv.GaussianBlur(img_gray, (3, 3), 0)
    laplacian = cv.Laplacian(img_gray, cv.CV_64F)
    img_lap = img_gray * laplacian
    # Canny Edge Detection
    edges = cv.Canny(image=img_blur, threshold1=100, threshold2=80)  # Canny Edge Detection
    edges_negative=abs(255-edges)
    # Display Canny Edge Detection Image
    # cv.imshow('Canny Edge Detection', edges)

    plt.subplot(2, 2, 1), plt.imshow(img_gray, cmap='gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(2, 2, 2), plt.imshow(img_blur, cmap='gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    # plt.show()
    # fig = plt.figure(1)
    # plt.imshow(edges_negative, cmap='gray')
    # plt.axis('off')
    convert_to_svg(edges_negative)
    draw_image('Output.svg')
