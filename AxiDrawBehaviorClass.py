import sys
from pyaxidraw import axidraw
import time
import numpy as np


class AxiDrawBehavior:

    def __int__(self):
        self.ad = axidraw.AxiDraw()           # AxiDraw Initialize class
        self.DXL_IDS = [1, 2]                 # define motors ID
        self.M1 = axidraw.Motor(self.DXL_IDS) # Initialize motors

    def homing(self):
        self.ad.interactive()
        connected = self.ad.connect()  # Open serial port to AxiDraw
        if not connected:
            sys.exit()  # end script
        self.ad.penup()
        self.ad.moveto(0, 0)  # Pen-up return home
        self.M1.Homeing()
        self.ad.disconnect()             # Close serial port to AxiDraw

    def draw_image(self, svg_image, mode='easy'):
        self.homing()
        try:
            self.M1.Enable_Torque()
            self.ad.interactive()  # Enter interactive mode
            connected = self.ad.connect()  # Open serial port to AxiDraw
            if not connected:
                sys.exit()  # end script
            self.ad.plot_setup(svg_image)
            self.ad.options.pen_pos_up = 72      # set pen-up position
            self.ad.options.pen_pos_down = 12
            if mode == 'easy':
                self.ad.options.speed_pendown = 8
                self.ad.options.speed_penup = 80
            elif mode == 'medium':
                self.ad.options.speed_pendown = 8
                self.ad.options.speed_penup = 50
            elif mode == 'hard':
                self.ad.options.speed_pendown = 6
                self.ad.options.speed_penup = 25
            self.ad.plot_run()
            self.ad.disconnect()  # Close serial port to AxiDraw
        except:
            print("Cant plot the image")

    def SpendTime(self):
        self.ad.interactive()  # Enter interactive mode
        connected = self.ad.connect()  # Open serial port to AxiDraw
        if not connected:
            sys.exit()  # end script
        self.ad.moveto(3, 0)  # robot go to middle
        t_start = time.time()
        t_end = 0
        temp1 = list(range(90, 270, 2))
        temp2 = temp1[::-1]
        pose = temp1 + [270] + temp2
        self.M1.Enable_Torque()
        self.M1.Write_Pos(180, 1)
        self.M1.Write_Pos(90, 2)
        while (t_end - t_start) <= 10:
            for i in pose:
                self.M1.Write_Pos(round(i), 2)
                # time.sleep(0.25)
                if not self.M1.inRange(self.M1.Read_Pos(2), 2):
                    raise Exception("Out of range, Homing failed, Try moving the arm and homing again")
            t_end = time.time()
        self.M1.Write_Pos(180, 2)
        self.ad.moveto(0, 0)             # robot return home
        self.ad.disconnect()             # Close serial port to AxiDraw

    def interference1(self):
        self.M1.Homeing()
        self.M1.Pointing()
        self.ad.interactive()  # Enter interactive mode
        connected = self.ad.connect()  # Open serial port to AxiDraw
        if not connected:
            sys.exit()  # end script
        flag = 0
        while flag < 5:
            self.ad.penup()
            self.ad.pendown()
            flag = flag + 1
        self.M1.Homeing()
        self.ad.disconnect()             # Close serial port to AxiDraw

    def interference2(self):
        self.M1.Homeing()
        self.M1.Write_Pos(298, 1)
        if not self.M1.inRange(self.M1.Read_Pos(1), 1):
            raise Exception("Out of range, pointing failed, Try moving the arm and try again")
        flag = 0
        # temp1 = list(range(156, 188, 2))
        # temp2 = temp1[::-1]
        # pose = temp1 + [188] + temp2
        self.M1.Write_Pos(140, 2)
        while flag < 10:
            # for i in pose:
            #     M1.Write_Pos(round(i), 2)
            # if not M1.inRange(M1.Read_Pos(2), 2):
            #     raise Exception("Out of range, pointing failed, Try moving the arm and try again")
            self.M1.Write_Pos(188, 2)
            time.sleep(0.5)
            self.M1.Write_Pos(140, 2)
            time.sleep(0.5)
            flag = flag + 1
        self.homing()

    def YourTurn(self):
        self.ad.interactive()
        connected = self.ad.connect()  # Open serial port to AxiDraw
        if not connected:
            sys.exit()  # end script
        self.ad.penup()
        self.ad.moveto(3, 0)  # Pen-up return home
        self.M1.Pointing()
        time.sleep(2)
        self.M1.Homeing()
        # ad.interactive()  # Enter interactive mode
        flag = 0
        while flag < 5:
            self.ad.penup()
            time.sleep(0.5)
            self.ad.pendown()
            flag = flag + 1
        self.M1.Homeing()
        self.M1.Pointing()
        time.sleep(2)
        self.ad.disconnect()  # Close serial port to AxiDraw
        self.homing()

    def Observe(self):
        self.M1.Homeing()
        try:
            self.ad.interactive()  # Enter interactive mode
            connected = self.ad.connect()  # Open serial port to AxiDraw
            if not connected:
                sys.exit()  # end script
            self.ad.moveto(0, 1)  # Absolute pen-up move, to (0 inch, 1 inch)
            t_start = time.time()
            t_end = 0
            temp1 = list(range(90, 270, 2))
            temp2 = temp1[::-1]
            pose = temp1 + [270] + temp2
            self.M1.Enable_Torque()
            self.M1.Write_Pos(180, 1)
            self.M1.Write_Pos(180, 2)
            while (t_end - t_start) <= 3:
                for i in pose:
                    self.M1.Write_Pos(round(i), 1)
                    # time.sleep(0.25)
                    if not self.M1.inRange(self.M1.Read_Pos(2), 2):
                        raise Exception("Out of range, Homing failed, Try moving the arm and homing again")
                t_end = time.time()
            self.M1.Write_Pos(180, 1)
            self.ad.moveto(4, 3)  # Absolute pen-up move, to (0 inch, 1 inch)
            t_start = time.time()
            t_end = 0
            temp1 = list(range(90, 270, 2))
            temp2 = temp1[::-1]
            pose = temp1 + [270] + temp2
            self.M1.Enable_Torque()
            self.M1.Write_Pos(180, 1)
            self.M1.Write_Pos(180, 2)
            while (t_end - t_start) <= 3:
                for i in pose:
                    self.M1.Write_Pos(round(i), 1)
                    # time.sleep(0.25)
                    if not self.M1.inRange(self.M1.Read_Pos(2), 2):
                        raise Exception("Out of range, Homing failed, Try moving the arm and homing again")
                t_end = time.time()
            self.M1.Write_Pos(180, 1)
            self.ad.moveto(0, 0)
            self.ad.disconnect()  # Close serial port to AxiDraw
        except:
            print("action stopped")

    #
    # def bowing():
    #     try:
    #         ad.interactive()  # Enter interactive mode
    #         connected = ad.connect()  # Open serial port to AxiDraw
    #         if not connected:
    #             sys.exit()  # end script
    #         ad.moveto(0, 0)  # Absolute pen-up move, to (0 inch, 1 inch)
    #         M1.Write_Pos(90, 2)
    #         M1.Write_Pos(50, 1)
    #         ad.disconnect()  # Close serial port to AxiDraw
    #     except:
    #         print("action stopped")
    #
    #
    # def signature():
    #     signature = 'signature.svg'
    #     draw_image(signature)
    #
    #
    # def waving():
    #     M1.Homeing()
    #     try:
    #         ad.interactive()  # Enter interactive mode
    #         connected = ad.connect()  # Open serial port to AxiDraw
    #         if not connected:
    #             sys.exit()  # end script
    #         t_start = time.time()
    #         t_end = 0
    #         temp1 = list(range(90, 270, 2))
    #         temp2 = temp1[::-1]
    #         pose = temp1 + [270] + temp2
    #         M1.Enable_Torque()
    #         M1.Write_Pos(180, 1)
    #         M1.Write_Pos(90, 2)
    #         flag = True
    #         while (t_end - t_start) <= 30:
    #             if flag:
    #                 ad.moveto(4, 3)  # Absolute pen-up move, to (0 inch, 1 inch)
    #                 flag = False
    #             else:
    #                 ad.moveto(0, 3)  # Absolute pen-up move, to (0 inch, 1 inch)
    #                 flag = True
    #             for i in pose:
    #                 M1.Write_Pos(round(i), 2)
    #                 # time.sleep(0.25)
    #                 if not M1.inRange(M1.Read_Pos(2), 2):
    #                     raise Exception("Out of range, Homing failed, Try moving the arm and homing again")
    #             t_end = time.time()
    #         M1.Write_Pos(180, 2)
    #         ad.disconnect()  # Close serial port to AxiDraw
    #         homing()
    #     except:
    #         print("action stopped")
    #
    #
    # def point_on(pose):
    #     M1.Enable_Torque()
    #     M1.Write_Pos(pose[0], 1)
    #     if not M1.inRange(M1.Read_Pos(2), 2):
    #         raise Exception("Out of range, pointing failed, Try moving the arm and try again")
    #     M1.Write_Pos(pose[1], 2)
    #     if not M1.inRange(M1.Read_Pos(2), 2):
    #         raise Exception("Out of range, pointing failed, Try moving the arm and try again")
    #
    #
    # def point_on_paper():
    #     ad.interactive()  # Enter interactive mode
    #     connected = ad.connect()  # Open serial port to AxiDraw
    #     if not connected:
    #         sys.exit()  # end script
    #     ad.moveto(6, 0)  # Absolute pen-up move, to (0 inch, 1 inch)
    #     M1.Enable_Torque()
    #     M1.Write_Pos(218, 1)
    #     if not M1.inRange(M1.Read_Pos(2), 2):
    #         raise Exception("Out of range, pointing failed, Try moving the arm and try again")
    #     M1.Write_Pos(228, 2)
    #     if not M1.inRange(M1.Read_Pos(2), 2):
    #         raise Exception("Out of range, pointing failed, Try moving the arm and try again")
    #     flag = 0
    #     while flag < 5:
    #         ad.penup()
    #         time.sleep(0.5)
    #         ad.pendown()
    #         flag = flag + 1
    #     ad.disconnect()  # Close serial port to AxiDraw
    #     homing()
    #
    #
    # def point_on_postcards():
    #     ad.interactive()  # Enter interactive mode
    #     connected = ad.connect()  # Open serial port to AxiDraw
    #     if not connected:
    #         sys.exit()  # end script
    #     M1.Enable_Torque()
    #     M1.Write_Pos(148, 1)
    #     if not M1.inRange(M1.Read_Pos(2), 2):
    #         raise Exception("Out of range, pointing failed, Try moving the arm and try again")
    #     M1.Write_Pos(230, 2)
    #     if not M1.inRange(M1.Read_Pos(2), 2):
    #         raise Exception("Out of range, pointing failed, Try moving the arm and try again")
    #     ad.moveto(6, 4)  # Absolute pen-up move, to (0 inch, 1 inch)
    #     flag = 0
    #     while flag < 5:
    #         ad.penup()
    #         time.sleep(0.5)
    #         ad.pendown()
    #         flag = flag + 1
    #     ad.moveto(0, 0)  # Absolute pen-up move, to (0 inch, 1 inch)
    #     ad.disconnect()  # Close serial port to AxiDraw
    #     homing()
    #
    #
    # def point_on_sit():
    #     ad.interactive()  # Enter interactive mode
    #     connected = ad.connect()  # Open serial port to AxiDraw
    #     if not connected:
    #         sys.exit()  # end script
    #     M1.Enable_Torque()
    #     ad.moveto(0, 4)  # Absolute pen-up move, to (0 inch, 1 inch)
    #     M1.Pointing()
    #     time.sleep(1)
    #     M1.Write_Pos(270, 1)
    #     if not M1.inRange(M1.Read_Pos(2), 2):
    #         raise Exception("Out of range, pointing failed, Try moving the arm and try again")
    #     M1.Write_Pos(115, 2)
    #     if not M1.inRange(M1.Read_Pos(2), 2):
    #         raise Exception("Out of range, pointing failed, Try moving the arm and try again")
    #     flag = 0
    #     while flag < 5:
    #         ad.penup()
    #         time.sleep(0.5)
    #         ad.pendown()
    #         flag = flag + 1
    #     ad.disconnect()  # Close serial port to AxiDraw
    #     homing()



if __name__ == '__main__':
    a = AxiDrawBehavior()
    a.homing()

    a.M1.Disable_Torque()
    a.ad.disconnect()             # Close serial port to AxiDraw
