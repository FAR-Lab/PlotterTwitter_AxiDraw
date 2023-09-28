import sys
from pyaxidraw import axidraw
import time
import numpy as np


def homing():
    ad.interactive()
    connected = ad.connect()  # Open serial port to AxiDraw
    if not connected:
        sys.exit()  # end script
    ad.penup()
    ad.moveto(0, 0)  # Pen-up return home
    M1.Homeing()
    ad.disconnect()             # Close serial port to AxiDraw


def draw_image(svg_image, mode='easy'):
    homing()
    try:
        M1.Enable_Torque()
        ad.interactive()  # Enter interactive mode
        connected = ad.connect()  # Open serial port to AxiDraw
        if not connected:
            sys.exit()  # end script
        ad.plot_setup(svg_image)
        ad.options.pen_pos_up = 72      # set pen-up position
        ad.options.pen_pos_down = 12
        if mode == 'easy':
            ad.options.speed_pendown = 8
            ad.options.speed_penup = 80
        elif mode == 'medium':
            ad.options.speed_pendown = 8
            ad.options.speed_penup = 50
        elif mode == 'hard':
            ad.options.speed_pendown = 6
            ad.options.speed_penup = 25
        ad.plot_run()
        ad.disconnect()  # Close serial port to AxiDraw
    except:
        print("Cant plot the image")


def SpendTime():
    ad.interactive()  # Enter interactive mode
    connected = ad.connect()  # Open serial port to AxiDraw
    if not connected:
        sys.exit()  # end script
    ad.moveto(3, 0)  # robot go to middle
    t_start = time.time()
    t_end = 0
    temp1 = list(range(90, 270, 2))
    temp2 = temp1[::-1]
    pose = temp1 + [270] + temp2
    M1.Enable_Torque()
    M1.Write_Pos(180, 1)
    M1.Write_Pos(90, 2)
    while (t_end - t_start) <= 10:
        for i in pose:
            M1.Write_Pos(round(i), 2)
            # time.sleep(0.25)
            if not M1.inRange(M1.Read_Pos(2), 2):
                raise Exception("Out of range, Homing failed, Try moving the arm and homing again")
        t_end = time.time()
    M1.Write_Pos(180, 2)
    ad.moveto(0, 0)             # robot return home
    ad.disconnect()             # Close serial port to AxiDraw


def interference1():
    M1.Homeing()
    M1.Pointing()
    ad.interactive()  # Enter interactive mode
    connected = ad.connect()  # Open serial port to AxiDraw
    if not connected:
        sys.exit()  # end script
    flag = 0
    while flag < 5:
        ad.penup()
        ad.pendown()
        flag = flag + 1
    M1.Homeing()
    ad.disconnect()             # Close serial port to AxiDraw


def interference2():
    M1.Homeing()
    M1.Write_Pos(298, 1)
    if not M1.inRange(M1.Read_Pos(1), 1):
        raise Exception("Out of range, pointing failed, Try moving the arm and try again")
    flag = 0
    # temp1 = list(range(156, 188, 2))
    # temp2 = temp1[::-1]
    # pose = temp1 + [188] + temp2
    M1.Write_Pos(140, 2)
    while flag < 10:
        # for i in pose:
        #     M1.Write_Pos(round(i), 2)
        # if not M1.inRange(M1.Read_Pos(2), 2):
        #     raise Exception("Out of range, pointing failed, Try moving the arm and try again")
        M1.Write_Pos(188, 2)
        time.sleep(0.5)
        M1.Write_Pos(140, 2)
        time.sleep(0.5)
        flag = flag + 1
    homing()


def YourTurn():
    ad.interactive()
    connected = ad.connect()  # Open serial port to AxiDraw
    if not connected:
        sys.exit()  # end script
    ad.penup()
    ad.moveto(3, 0)  # Pen-up return home
    M1.Pointing()
    time.sleep(2)
    M1.Homeing()
    # ad.interactive()  # Enter interactive mode
    flag = 0
    while flag < 5:
        ad.penup()
        time.sleep(0.5)
        ad.pendown()
        flag = flag + 1
    M1.Homeing()
    M1.Pointing()
    time.sleep(2)
    ad.disconnect()  # Close serial port to AxiDraw
    homing()


def Observe():
    M1.Homeing()
    try:
        ad.interactive()  # Enter interactive mode
        connected = ad.connect()  # Open serial port to AxiDraw
        if not connected:
            sys.exit()  # end script
        ad.moveto(0, 1)  # Absolute pen-up move, to (0 inch, 1 inch)
        t_start = time.time()
        t_end = 0
        temp1 = list(range(90, 270, 2))
        temp2 = temp1[::-1]
        pose = temp1 + [270] + temp2
        M1.Enable_Torque()
        M1.Write_Pos(180, 1)
        M1.Write_Pos(180, 2)
        while (t_end - t_start) <= 3:
            for i in pose:
                M1.Write_Pos(round(i), 1)
                # time.sleep(0.25)
                if not M1.inRange(M1.Read_Pos(2), 2):
                    raise Exception("Out of range, Homing failed, Try moving the arm and homing again")
            t_end = time.time()
        M1.Write_Pos(180, 1)
        ad.moveto(4, 3)  # Absolute pen-up move, to (0 inch, 1 inch)
        t_start = time.time()
        t_end = 0
        temp1 = list(range(90, 270, 2))
        temp2 = temp1[::-1]
        pose = temp1 + [270] + temp2
        M1.Enable_Torque()
        M1.Write_Pos(180, 1)
        M1.Write_Pos(180, 2)
        while (t_end - t_start) <= 3:
            for i in pose:
                M1.Write_Pos(round(i), 1)
                # time.sleep(0.25)
                if not M1.inRange(M1.Read_Pos(2), 2):
                    raise Exception("Out of range, Homing failed, Try moving the arm and homing again")
            t_end = time.time()
        M1.Write_Pos(180, 1)
        ad.moveto(0, 0)
        ad.disconnect()  # Close serial port to AxiDraw
    except:
        print("action stopped")


def bowing():
    try:
        ad.interactive()  # Enter interactive mode
        connected = ad.connect()  # Open serial port to AxiDraw
        if not connected:
            sys.exit()  # end script
        ad.moveto(0, 0)  # Absolute pen-up move, to (0 inch, 1 inch)
        M1.Write_Pos(90, 2)
        M1.Write_Pos(50, 1)
        ad.disconnect()  # Close serial port to AxiDraw
    except:
        print("action stopped")


def signature():
    signature = 'signature.svg'
    draw_image(signature)


def waving():
    M1.Homeing()
    try:
        ad.interactive()  # Enter interactive mode
        connected = ad.connect()  # Open serial port to AxiDraw
        if not connected:
            sys.exit()  # end script
        t_start = time.time()
        t_end = 0
        temp1 = list(range(90, 270, 2))
        temp2 = temp1[::-1]
        pose = temp1 + [270] + temp2
        M1.Enable_Torque()
        M1.Write_Pos(180, 1)
        M1.Write_Pos(90, 2)
        flag = True
        while (t_end - t_start) <= 30:
            if flag:
                ad.moveto(4, 3)  # Absolute pen-up move, to (0 inch, 1 inch)
                flag = False
            else:
                ad.moveto(0, 3)  # Absolute pen-up move, to (0 inch, 1 inch)
                flag = True
            for i in pose:
                M1.Write_Pos(round(i), 2)
                # time.sleep(0.25)
                if not M1.inRange(M1.Read_Pos(2), 2):
                    raise Exception("Out of range, Homing failed, Try moving the arm and homing again")
            t_end = time.time()
        M1.Write_Pos(180, 2)
        ad.disconnect()  # Close serial port to AxiDraw
        homing()
    except:
        print("action stopped")


def point_on(pose):
    M1.Enable_Torque()
    M1.Write_Pos(pose[0], 1)
    if not M1.inRange(M1.Read_Pos(2), 2):
        raise Exception("Out of range, pointing failed, Try moving the arm and try again")
    M1.Write_Pos(pose[1], 2)
    if not M1.inRange(M1.Read_Pos(2), 2):
        raise Exception("Out of range, pointing failed, Try moving the arm and try again")


def point_on_paper():
    ad.interactive()  # Enter interactive mode
    connected = ad.connect()  # Open serial port to AxiDraw
    if not connected:
        sys.exit()  # end script
    ad.moveto(6, 0)  # Absolute pen-up move, to (0 inch, 1 inch)
    M1.Enable_Torque()
    M1.Write_Pos(218, 1)
    if not M1.inRange(M1.Read_Pos(2), 2):
        raise Exception("Out of range, pointing failed, Try moving the arm and try again")
    M1.Write_Pos(228, 2)
    if not M1.inRange(M1.Read_Pos(2), 2):
        raise Exception("Out of range, pointing failed, Try moving the arm and try again")
    flag = 0
    while flag < 5:
        ad.penup()
        time.sleep(0.5)
        ad.pendown()
        flag = flag + 1
    ad.disconnect()  # Close serial port to AxiDraw
    homing()


def point_on_postcards():
    ad.interactive()  # Enter interactive mode
    connected = ad.connect()  # Open serial port to AxiDraw
    if not connected:
        sys.exit()  # end script
    M1.Enable_Torque()
    M1.Write_Pos(148, 1)
    if not M1.inRange(M1.Read_Pos(2), 2):
        raise Exception("Out of range, pointing failed, Try moving the arm and try again")
    M1.Write_Pos(230, 2)
    if not M1.inRange(M1.Read_Pos(2), 2):
        raise Exception("Out of range, pointing failed, Try moving the arm and try again")
    ad.moveto(6, 4)  # Absolute pen-up move, to (0 inch, 1 inch)
    flag = 0
    while flag < 5:
        ad.penup()
        time.sleep(0.5)
        ad.pendown()
        flag = flag + 1
    ad.moveto(0, 0)  # Absolute pen-up move, to (0 inch, 1 inch)
    ad.disconnect()  # Close serial port to AxiDraw
    homing()




if __name__ == '__main__':
    ad = axidraw.AxiDraw() # Initialize class
    DXL_IDS = [1, 2] # define motors ID
    M1 = axidraw.Motor(DXL_IDS) # Initialize motors
    homing()
    print("spendtime")
    SpendTime()
    time.sleep(1)
    print("interapt1")
    interference1()
    time.sleep(1)
    print("interapt2")
    interference2()
    time.sleep(1)
    print("yourturn")
    YourTurn()
    time.sleep(1)
    Observe()
    time.sleep(1)
    point_on_paper()
    time.sleep(1)
    # signature()
    waving()
    time.sleep(1)
    point_on_postcards()
    time.sleep(1)
    # draw_image('postcard1_.svg', mode='medium')
    bowing()
    time.sleep(1)
    homing()
    print("Done")
    time.sleep(1)
    M1.Disable_Torque()
    ad.disconnect()             # Close serial port to AxiDraw
