import sys
from pyaxidraw import axidraw
import time
import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import control_camera_draw as cam1
import control_camera_zed as cam2
import AxiDrawBehavior as action
from threading import Thread


def Make_Attention():
    while True:
        action.waving()
        action.interference1()
        if cv.waitKey(1) == ord('s'):
            break


if __name__ == '__main__':
    ad = axidraw.AxiDraw()  # Initialize class
    DXL_IDS = [1, 2]  # define motors ID
    M1 = axidraw.Motor(DXL_IDS)
    # Welcoming
    action.homing()
    Make_Attention()
    action.M1.Pointing() # maybe point detaction
    action.point_on_sit()


    # Colabortion part
