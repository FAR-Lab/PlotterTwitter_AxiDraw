import sys
from pyaxidraw import axidraw
import time
import numpy as np
import keyboard


def homing():
    ad.interactive()
    connected = ad.connect()  # Open serial port to AxiDraw
    if not connected:
        sys.exit()  # end script
    ad.penup()
    ad.moveto(0, 0)  # Pen-up return home
    M1.Homeing()
    ad.disconnect()             # Close serial port to AxiDraw
    time.sleep(1)


def draw_image(svg_image, mode='easy', pen_pos_down=40):
    homing()
    try:
        M1.Enable_Torque()
        ad.interactive()  # Enter interactive mode
        connected = ad.connect()  # Open serial port to AxiDraw
        if not connected:
            sys.exit()  # end script
        ad.plot_setup(svg_image)
        ad.options.pen_pos_up = 72      # set pen-up position
        ad.options.pen_pos_down = pen_pos_down
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
    ad.disconnect()             # Close serial port to AxiDraw


def Thinking():
    M1.Homeing()
    ad.interactive()
    connected = ad.connect()  # Open serial port to AxiDraw
    if not connected:
        sys.exit()  # end script
    ad.penup()
    ad.moveto(1, 0)  # Pen-up return home
    ad.moveto(1, 2)

    # M1.Write_Pos(298, 1)
    # if not M1.inRange(M1.Read_Pos(1), 1):
    #     raise Exception("Out of range, pointing failed, Try moving the arm and try again")
    flag = 0
    temp1 = list(range(156, 188, 1))
    temp2 = temp1[::-1]
    pose = temp1 + [188] + temp2
    M1.Write_Pos(140, 2)

    while flag < 2:
        for i in pose:
            M1.Write_Pos(round(i), 2)
        if not M1.inRange(M1.Read_Pos(2), 2):
            raise Exception("Out of range, pointing failed, Try moving the arm and try again")
        flag = flag + 1
    ad.moveto(2, 2)
    time.sleep(0.5)
    ad.moveto(2, 0)
    time.sleep(0.5)
    ad.moveto(3, 0)
    time.sleep(0.5)
    ad.moveto(3, 2)
    flag = 0
    M1.Write_Pos(140, 2)
    while flag < 2:
        for i in pose:
            M1.Write_Pos(round(i), 2)
        if not M1.inRange(M1.Read_Pos(2), 2):
            raise Exception("Out of range, pointing failed, Try moving the arm and try again")
        flag = flag + 1
    ad.disconnect()
    homing()


def YourTurn():
    ad.interactive()
    connected = ad.connect()  # Open serial port to AxiDraw
    if not connected:
        sys.exit()  # end script
    ad.penup()
    ad.options.pen_pos_down = 45
    ad.moveto(3, 1)  # Pen-up return home
    M1.Pointing()
    time.sleep(1)
    ad.disconnect()  # Close serial port to AxiDraw
    bowing_right()
    ad.interactive()
    connected = ad.connect()  # Open serial port to AxiDraw
    if not connected:
        sys.exit()  # end script
    # ad.interactive()  # Enter interactive mode
    flag = 0
    while flag < 3:
        ad.penup()
        time.sleep(0.5)
        ad.pendown()
        flag = flag + 1
    pose = range(120, 200, 1)
    # pose = pose[::-1]
    for i in pose:
        M1.Write_Pos(round(i), 2)
        if not M1.inRange(M1.Read_Pos(2), 2):
            raise Exception("Out of range, Homing failed, Try moving the arm and homing again")
    ad.disconnect()  # Close serial port to AxiDraw


def ColorsYourTurn():
    ad.interactive()
    connected = ad.connect()  # Open serial port to AxiDraw
    if not connected:
        sys.exit()  # end script
    ad.penup()
    ad.options.pen_pos_down = 45
    ad.moveto(0, 0)  # Pen-up return home
    M1.Pointing()
    time.sleep(1)
    ad.disconnect()  # Close serial port to AxiDraw
    bowing_left()
    ad.interactive()
    connected = ad.connect()  # Open serial port to AxiDraw
    if not connected:
        sys.exit()  # end script
    flag = 0
    while flag < 3:
        ad.penup()
        time.sleep(0.5)
        ad.pendown()
        flag = flag + 1
    ad.disconnect()  # Close serial port to AxiDraw
    time.sleep(0.5)
    ad.interactive()  # Enter interactive mode
    connected = ad.connect()  # Open serial port to AxiDraw
    if not connected:
        sys.exit()  # end script
    M1.Write_Pos(180, 1)
    pose = range(120, 180, 1)
    pose = pose[::-1]
    for i in pose:
        M1.Write_Pos(round(i), 2)
        if not M1.inRange(M1.Read_Pos(2), 2):
            raise Exception("Out of range, Homing failed, Try moving the arm and homing again")
    flag = 0
    while flag < 3:
        ad.penup()
        time.sleep(0.5)
        ad.pendown()
        flag = flag + 1
    ad.disconnect()  # Close serial port to AxiDraw
    bowing_left()
    print("wait until finish draw")
    input()


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
                if not M1.inRange(M1.Read_Pos(1), 1):
                    raise Exception("Out of range, Homing failed, Try moving the arm and homing again")
            t_end = time.time()
        M1.Write_Pos(180, 1)
        ad.moveto(0, 0)
        ad.disconnect()  # Close serial port to AxiDraw
    except:
        print("action stopped")


def bowing_right():
    try:
        ad.interactive()  # Enter interactive mode
        connected = ad.connect()  # Open serial port to AxiDraw
        if not connected:
            sys.exit()  # end script
        ad.moveto(5, 0)  # Absolute pen-up move, to (0 inch, 1 inch)
        M1.Write_Pos(210, 1)
        pose = range(120, 180, 1)
        pose = pose[::-1]
        for i in pose:
            M1.Write_Pos(round(i), 2)
            if not M1.inRange(M1.Read_Pos(2), 2):
                raise Exception("Out of range, Homing failed, Try moving the arm and homing again")

        ad.disconnect()  # Close serial port to AxiDraw
    except:
        print("action stopped")


def bowing_left():
    try:
        ad.interactive()  # Enter interactive mode
        connected = ad.connect()  # Open serial port to AxiDraw
        if not connected:
            sys.exit()  # end script
        ad.moveto(0, 0)  # Absolute pen-up move, to (0 inch, 1 inch)
        M1.Write_Pos(120, 1)
        pose = range(180, 222, 1)
        for i in pose:
            M1.Write_Pos(round(i), 2)
            if not M1.inRange(M1.Read_Pos(2), 2):
                raise Exception("Out of range, Homing failed, Try moving the arm and homing again")
        ad.disconnect()  # Close serial port to AxiDraw
    except:
        print("action stopped")


def signature():
    signature = 'postcard_templets/signature.svg'
    draw_image(signature, pen_pos_down=pen[1])


def waving():
    M1.Homeing()
    try:
        ad.interactive()  # Enter interactive mode
        connected = ad.connect()  # Open serial port to AxiDraw
        if not connected:
            sys.exit()  # end script
        t_start = time.time()
        t_end = 0
        temp1 = list(range(90, 270, 4))
        temp2 = temp1[::-1]
        pose = temp2 + [90] + temp1
        M1.Enable_Torque()
        M1.Write_Pos(180, 1)
        M1.Write_Pos(270, 2)
        ad.moveto(0, 4)  # Absolute pen-up move, to (0 inch, 1 inch)
        flag = True
        while (t_end - t_start) <= 15:
            if flag:
                ad.moveto(3, 4)  # Absolute pen-up move, to (0 inch, 1 inch)
                flag = False
            else:
                ad.moveto(0, 4)  # Absolute pen-up move, to (0 inch, 1 inch)
                flag = True
            for i in pose:
                M1.Write_Pos(round(i), 2)
                if not M1.inRange(M1.Read_Pos(2), 2):
                    raise Exception("Out of range, Homing failed, Try moving the arm and homing again")
            t_end = time.time()
        ad.disconnect()  # Close serial port to AxiDraw
    except:
        print("action stopped")


def goodbye():
    try:
        ad.interactive()  # Enter interactive mode
        connected = ad.connect()  # Open serial port to AxiDraw
        if not connected:
            sys.exit()  # end script
        t_start = time.time()
        t_end = 0
        temp1 = list(range(90, 270, 4))
        temp2 = temp1[::-1]
        pose = temp2 + [90] + temp1
        M1.Enable_Torque()
        M1.Write_Pos(180, 1)
        M1.Write_Pos(270, 2)
        ad.moveto(0, 4)  # Absolute pen-up move, to (0 inch, 1 inch)
        flag = True
        while (t_end - t_start) <= 6:
            for i in pose:
                M1.Write_Pos(round(i), 2)
                if not M1.inRange(M1.Read_Pos(2), 2):
                    raise Exception("Out of range, Homing failed, Try moving the arm and homing again")
            t_end = time.time()
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
    ad.moveto(0, 2)  # Absolute pen-up move, to (0 inch, 1 inch)
    M1.Enable_Torque()
    M1.Write_Pos(188, 1)
    if not M1.inRange(M1.Read_Pos(2), 2):
        raise Exception("Out of range, pointing failed, Try moving the arm and try again")
    M1.Write_Pos(127, 2)
    if not M1.inRange(M1.Read_Pos(2), 2):
        raise Exception("Out of range, pointing failed, Try moving the arm and try again")
    flag = 0
    while flag < 3:
        ad.penup()
        time.sleep(0.5)
        ad.pendown()
        flag = flag + 1
    ad.disconnect()  # Close serial port to AxiDraw
    bowing_left()


def point_on_postcards():
    ad.interactive()  # Enter interactive mode
    connected = ad.connect()  # Open serial port to AxiDraw
    if not connected:
        sys.exit()  # end script
    M1.Enable_Torque()
    M1.Write_Pos(197, 1)
    if not M1.inRange(M1.Read_Pos(2), 2):
        raise Exception("Out of range, pointing failed, Try moving the arm and try again")
    M1.Write_Pos(191, 2)
    if not M1.inRange(M1.Read_Pos(2), 2):
        raise Exception("Out of range, pointing failed, Try moving the arm and try again")
    ad.moveto(6, 0)  # Absolute pen-up move, to (0 inch, 1 inch)
    flag = 0
    while flag < 3:
        ad.penup()
        time.sleep(0.5)
        ad.pendown()
        flag = flag + 1
    # ad.moveto(0, 0)  # Absolute pen-up move, to (0 inch, 1 inch)
    ad.disconnect()  # Close serial port to AxiDraw


def point_on_sit():
    ad.interactive()  # Enter interactive mode
    connected = ad.connect()  # Open serial port to AxiDraw
    if not connected:
        sys.exit()  # end script
    M1.Enable_Torque()
    ad.moveto(0, 4)  # Absolute pen-up move, to (0 inch, 1 inch)
    M1.Pointing()
    time.sleep(0.5)
    M1.Write_Pos(270, 1)
    if not M1.inRange(M1.Read_Pos(2), 2):
        raise Exception("Out of range, pointing failed, Try moving the arm and try again")
    M1.Write_Pos(120, 2)
    if not M1.inRange(M1.Read_Pos(2), 2):
        raise Exception("Out of range, pointing failed, Try moving the arm and try again")
    flag = 0
    while flag < 5:
        ad.penup()
        time.sleep(0.5)
        ad.pendown()
        flag = flag + 1
    ad.disconnect()  # Close serial port to AxiDraw
    print("Did someone sits or not?")
    sit = input()
    if sit == 'not':
        point_on_sit()


def Make_Attention():
    while True:
        waving()
        interference1()
        print("wait for out?")
        out = input()
        if out == 'out':
            break


def No():
    M1.Homeing()
    try:
        ad.interactive()  # Enter interactive mode
        connected = ad.connect()  # Open serial port to AxiDraw
        if not connected:
            sys.exit()  # end script
        t_start = time.time()
        t_end = 0
        temp1 = list(range(130, 220, 1))
        temp2 = temp1[::-1]
        pose = temp1 + [220] + temp2
        M1.Enable_Torque()
        M1.Write_Pos(220, 1)
        M1.Write_Pos(270, 2)
        ad.moveto(0, 4)  # Absolute pen-up move, to (0 inch, 1 inch)
        M1.Write_Pos(356, 2)
        while (t_end - t_start) <= 5:
            # ad.moveto(2, 4)  # Absolute pen-up move, to (0 inch, 1 inch)
            M1.Write_Pos(130, 1)
            if not M1.inRange(M1.Read_Pos(1), 1):
                raise Exception("Out of range, Homing failed, Try moving the arm and homing again")
            time.sleep(0.75)
            M1.Write_Pos(220, 1)
            if not M1.inRange(M1.Read_Pos(1), 1):
                raise Exception("Out of range, Homing failed, Try moving the arm and homing again")
            time.sleep(0.75)
            t_end = time.time()
        M1.Write_Pos(270, 2)
        M1.Write_Pos(180, 1)
        ad.disconnect()  # Close serial port to AxiDraw
        homing()
    except:
        print("action stopped")


def demo_wizard():
    print("welcome or go?")
    temp = input()
    if temp != "go":
        # Welcoming
        homing()
        Make_Attention()
        # M1.Pointing()  # maybe point detaction
        point_on_sit()
    # Colabortion part
        point_on_paper()
        print("wait for put a paper or again")
        temp = input()
        if temp == 'again':
            point_on_paper()
            print("wait for put a paper or again")
            input()
        point_on_postcards()
        time.sleep(0.5)
        bowing_right()

    while True:
        print("wait for input, start the while loop")
        postcard = input()
        if postcard == '1':
            Thinking()
            print("draw cornell")
            draw_image('postcard_templets/postcard1_cornell.svg',pen_pos_down=pen[0])
            ColorsYourTurn()

        elif postcard == '2':
            SpendTime()
            print("draw NYC1")
            draw_image('postcard_templets/postcard1_NYC_part1.svg',pen_pos_down=pen[0])
            ColorsYourTurn()
            print("wait for flag")
            flag = input()
            if flag == 'draw':
                Observe()
                print("draw NYC2")
                draw_image('postcard_templets/postcard1_NYC_part2.svg', pen_pos_down=pen[1])
                ColorsYourTurn()
            print("wait for flag")
            flag = input()
            if flag == 'draw':
                SpendTime()
                print("draw NYC3")
                draw_image('postcard_templets/postcard1_NYC_part3.svg', pen_pos_down=pen[0])
                ColorsYourTurn()

        elif postcard == '3':
            Thinking()
            draw_image('postcard_templets/postcard_hall_part2.svg', pen_pos_down=pen[0])
            ColorsYourTurn()
            flag = input()
            Observe()
            if flag == 'draw':
                print("draw hallawin2")
                draw_image('postcard_templets/postcard_hall_part1.svg', pen_pos_down=pen[2])
                ColorsYourTurn()
            flag = input()
            if flag == 'draw':
                print("draw hallawin3")
                draw_image('postcard_templets/postcard_hall_part3.svg', pen_pos_down=pen[1])
                ColorsYourTurn()

        elif postcard == '4':
            print("draw or not")
            flag = input()
            if flag == 'draw':
                Thinking()
                draw_image('postcard_templets/postcard1_val2_part1.svg', pen_pos_down=pen[0])
                ColorsYourTurn()
                print("valsign or not")
                flag = input()
            else:
                Thinking()
                print("draw Vallday1")
                draw_image('postcard_templets/postcard1_val.svg', pen_pos_down=pen[0])
                ColorsYourTurn()
                print("valsign or not")
                flag = input()
            if flag == 'valsign':
                draw_image('postcard_templets/postcard1_val2_part2.svg', pen_pos_down=pen[1])
                ColorsYourTurn()

        elif postcard == 'bee':
            Thinking()
            draw_image('postcard_templets/bee.svg', pen_pos_down=pen[2])
            ColorsYourTurn()

        elif postcard == 'sign':
            signature()
            break

        elif postcard == 'done':
            Observe()
            break
        else:
            No()
            point_on_postcards()
            bowing_right()


if __name__ == '__main__':
    pen1 = [45, 44, 42]
    pen2 = [28, 27, 25]
    pen = pen1
    ad = axidraw.AxiDraw() # Initialize class
    DXL_IDS = [1, 2] # define motors ID
    M1 = axidraw.Motor(DXL_IDS) # Initialize motors
    M1.Enable_Torque()
    homing()
    demo_wizard()
    YourTurn()
    print("wait for Good Bye")
    input()
    goodbye()
    print("Done")
    time.sleep(1)
    while True:
        again = input()
        if again == "done":
            homing()
            time.sleep(0.25)
            M1.Disable_Torque()
            ad.disconnect()             # Close serial port to AxiDraw
            print("Finished")
            break
        else:
            print("played again")
            demo_wizard()
            YourTurn()
            print("wait for Good Bye")
            input()
            goodbye()
            print("Done")
