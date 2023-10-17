#!/usr/bin/env python
# -*- coding: utf-8 -*-

################################################################################
# Copyright 2017 ROBOTIS CO., LTD.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

#*******************************************************************************
#***********************     Bulk Read and Bulk Write Example      ***********************
#  Required Environment to run this example :
#    - Protocol 2.0 supported DYNAMIXEL(X, P, PRO/PRO(A), MX 2.0 series). Note that the XL320 does not support Bulk Read and Bulk Write.
#    - DYNAMIXEL Starter Set (U2D2, U2D2 PHB, 12V SMPS)
#  How to use the example :
#    - Select the DYNAMIXEL in use at the MY_DXL in the example code.
#    - Build and Run from proper architecture subdirectory.
#    - For ARM based SBCs such as Raspberry Pi, use linux_sbc subdirectory to build and run.
#    - https://emanual.robotis.com/docs/en/software/dynamixel/dynamixel_sdk/overview/
#  Author: Ryu Woon Jung (Leon)
#  Maintainer : Zerom, Will Son
# *******************************************************************************

import os

if os.name == 'nt':
    import msvcrt

    def getch():
        return msvcrt.getch().decode()
else:
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    def getch():
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

from dynamixel_sdk import *                    # Uses Dynamixel SDK library


#********* DYNAMIXEL Model definition *********
#***** (Use only one definition at a time) *****
MY_DXL = 'X_SERIES'       # X330 (5.0 V recommended), X430, X540, 2X430
# MY_DXL = 'MX_SERIES'    # MX series with 2.0 firmware update.
# MY_DXL = 'PRO_SERIES'   # H54, H42, M54, M42, L54, L42
# MY_DXL = 'PRO_A_SERIES' # PRO series with (A) firmware update.
# MY_DXL = 'P_SERIES'     # PH54, PH42, PM54

# Control table address is different in Dynamixel model
ADDR_TORQUE_ENABLE          = 64
ADDR_LED_RED                = 65
LEN_LED_RED                 = 1         # Data Byte Length
ADDR_GOAL_POSITION          = 116
LEN_GOAL_POSITION           = 4         # Data Byte Length
ADDR_PRESENT_POSITION       = 132
LEN_PRESENT_POSITION        = 4         # Data Byte Length
DXL_MINIMUM_POSITION_VALUE  = 1042         # Refer to the Minimum Position Limit of product eManual
DXL_MAXIMUM_POSITION_VALUE  = 2700      # Refer to the Maximum Position Limit of product eManual
BAUDRATE                    = 57600

# DYNAMIXEL Protocol Version (1.0 / 2.0)
# https://emanual.robotis.com/docs/en/dxl/protocol2/
PROTOCOL_VERSION            = 2.0            # See which protocol version is used in the Dynamixel

# Make sure that each DYNAMIXEL ID should have unique ID.
DXL1_ID                     = 1                 # Dynamixel#1 ID : 1
DXL2_ID                     = 2                 # Dynamixel#1 ID : 2

# Use the actual port assigned to the U2D2.
# ex) Windows: "COM*", Linux: "/dev/ttyUSB*", Mac: "/dev/tty.usbserial-*"
DEVICENAME                  = 'COM9'

TORQUE_ENABLE               = 1                 # Value for enabling the torque
TORQUE_DISABLE              = 0                 # Value for disabling the torque
DXL_MOVING_STATUS_THRESHOLD = 10                # Dynamixel moving status threshold
ESC_ASCII_VALUE             = 0x1b

index = 0
dxl_goal_position = [DXL_MINIMUM_POSITION_VALUE, DXL_MAXIMUM_POSITION_VALUE]        # Goal position
dxl_led_value = [0x00, 0x01]                                                        # Dynamixel LED value for write
dxl_comm_result = COMM_TX_FAIL                              # Communication result
dxl_addparam_result = 0                                     # AddParam result
dxl_getdata_result = 0                                      # GetParam result

dxl_error = 0                                               # Dynamixel error
dxl1_present_position = 0                                   # Present position
dxl2_present_position = 0

# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler(DEVICENAME)

# Initialize PacketHandler instance
# Set the protocol version
# Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
packetHandler = PacketHandler(PROTOCOL_VERSION)

# Initialize Groupsyncwrite instance
groupwrite_num = GroupSyncWrite(portHandler, PROTOCOL_VERSION, ADDR_GOAL_POSITION, LEN_GOAL_POSITION)

# Initialize Groupsyncread Structs for Present Position
groupread_num = GroupSyncRead(port=portHandler, ph=PROTOCOL_VERSION, start_address=ADDR_PRESENT_POSITION, data_length=LEN_PRESENT_POSITION)

# Initialize GroupBulkWrite instance
groupBulkWrite = GroupBulkWrite(portHandler, packetHandler)

# Initialize GroupBulkRead instace for Present Position
groupBulkRead = GroupBulkRead(portHandler, packetHandler)

# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    getch()
    quit()


# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    getch()
    quit()

# Enable Dynamixel#1 Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel#%d has been successfully connected" % DXL1_ID)

# Enable Dynamixel#2 Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL2_ID, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel#%d has been successfully connected" % DXL2_ID)

# Add parameter storage for Dynamixel#1 present position value
dxl_addparam_result = groupread_num.addParam(DXL1_ID)
if dxl_addparam_result != 1:
    print("[ID:%03d] groupSyncRead addparam failed" % (DXL1_ID))
    quit()

# Add parameter storage for Dynamixel#2 present position value
dxl_addparam_result = groupread_num.addParam(DXL2_ID)
if dxl_addparam_result != 1:
    print("[ID:%03d] groupSyncRead addparam failed" % (DXL2_ID))
    quit()

while 1:
    print("Press any key to continue! (or press ESC to quit!)")
    if getch() == chr(ESC_ASCII_VALUE):
        break
    # Allocate goal position value into byte array
    param_goal_position = [DXL_LOBYTE(DXL_LOWORD(dxl_goal_position[index])),
                           DXL_HIBYTE(DXL_LOWORD(dxl_goal_position[index])),
                           DXL_LOBYTE(DXL_HIWORD(dxl_goal_position[index])),
                           DXL_HIBYTE(DXL_HIWORD(dxl_goal_position[index]))]
    print(param_goal_position, index)
    # Add Dynamixel#1 goal position value to the Syncwrite storage
    dxl_addparam_result = groupwrite_num.addParam(DXL1_ID, param_goal_position)
    print(dxl_addparam_result)
    if dxl_addparam_result != 1:
        print("[ID:%03d] groupSyncWrite addparam failed" % (DXL1_ID))
        quit()

    # Add Dynamixel#2 goal position value to the Syncwrite parameter storage
    dxl_addparam_result = groupwrite_num.addParam(DXL2_ID, param_goal_position)
    if dxl_addparam_result != 1:
        print("[ID:%03d] groupSyncWrite addparam failed" % DXL2_ID)
        quit()

    # Syncwrite goal position
    # angle = DXL_MAXIMUM_POSITION_VALUE
    #
    # angle = round(angle * (4095 / 360))  # degree to tic
    # if angle > 4095:
    #     angle = angle - 4095
    # elif angle < 0:
    #     angle = angle + 4095
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL1_ID,
                                                                   ADDR_GOAL_POSITION,dxl_goal_position[index])
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))

    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL2_ID, ADDR_GOAL_POSITION, dxl_goal_position[index])
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))

    # Clear syncwrite parameter storage
    groupwrite_num.clearParam()

    while 1:
        dxl1_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL1_ID,
                                                                                       ADDR_PRESENT_POSITION)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))

        dxl2_present_position, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL2_ID,
                                                                                       ADDR_PRESENT_POSITION)
        if dxl_comm_result != COMM_SUCCESS:
            print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        elif dxl_error != 0:
            print("%s" % packetHandler.getRxPacketError(dxl_error))

        # # Syncread present position
        # dxl_comm_result = groupread_num.txRxPacket()
        # if dxl_comm_result != COMM_SUCCESS:
        #     print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
        #
        # # Check if groupsyncread data of Dynamixel#1 is available
        # dxl_getdata_result = groupread_num.isAvailable(DXL1_ID, ADDR_PRESENT_POSITION, LEN_PRESENT_POSITION)
        # if dxl_getdata_result != 1:
        #     print("[ID:%03d] groupSyncRead getdata failed" % DXL1_ID)
        #     quit()
        #
        # # Check if groupsyncread data of Dynamixel#2 is available
        # dxl_getdata_result = groupread_num.isAvailable(DXL2_ID, ADDR_PRESENT_POSITION, LEN_PRESENT_POSITION)
        # if dxl_getdata_result != 1:
        #     print("[ID:%03d] groupSyncRead getdata failed" % DXL2_ID)
        #     quit()

        # Get Dynamixel#1 present position value
        # dxl1_present_position = groupread_num.getData(DXL1_ID, ADDR_PRESENT_POSITION,
        #                                                            LEN_PRESENT_POSITION)
        #
        # # Get Dynamixel#2 present position value
        # dxl2_present_position = groupread_num.getData(DXL2_ID, ADDR_PRESENT_POSITION,
        #                                                            LEN_PRESENT_POSITION)

        print("[ID:%03d] GoalPos:%03d  PresPos:%03d\t[ID:%03d] GoalPos:%03d  PresPos:%03d\n" % (DXL1_ID,
                                                                                                dxl_goal_position[index],
                                                                                                dxl1_present_position,
                                                                                                DXL2_ID,
                                                                                                dxl_goal_position[index],
                                                                                                dxl2_present_position))

        if not ((abs(dxl_goal_position[index] - dxl1_present_position) > DXL_MOVING_STATUS_THRESHOLD) or
                (abs(dxl_goal_position[index] - dxl2_present_position) > DXL_MOVING_STATUS_THRESHOLD)):
            break

    # Change goal position
    if index == 0:
        index = 1
    else:
        index = 0

# Clear syncread parameter storage
groupread_num.clearParam()

# Disable Dynamixel#1 Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

# Disable Dynamixel#2 Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL2_ID, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

# Close port
portHandler.closePort()









# # Enable Dynamixel#1 Torque
# dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
# if dxl_comm_result != COMM_SUCCESS:
#     print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
# elif dxl_error != 0:
#     print("%s" % packetHandler.getRxPacketError(dxl_error))
# else:
#     print("Dynamixel#%d has been successfully connected" % DXL1_ID)
#
# # Enable Dynamixel#2 Torque
# dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL2_ID, ADDR_TORQUE_ENABLE, TORQUE_ENABLE)
# if dxl_comm_result != COMM_SUCCESS:
#     print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
# elif dxl_error != 0:
#     print("%s" % packetHandler.getRxPacketError(dxl_error))
# else:
#     print("Dynamixel#%d has been successfully connected" % DXL2_ID)
#
# # Add parameter storage for Dynamixel#1 present position
# dxl_addparam_result = groupBulkRead.addParam(DXL1_ID, ADDR_PRESENT_POSITION, LEN_PRESENT_POSITION)
# if dxl_addparam_result != True:
#     print("[ID:%03d] groupBulkRead addparam failed" % DXL1_ID)
#     quit()
#
# # Add parameter storage for Dynamixel#2 LED value
# dxl_addparam_result = groupBulkRead.addParam(DXL2_ID, ADDR_LED_RED, LEN_LED_RED)
# if dxl_addparam_result != True:
#     print("[ID:%03d] groupBulkRead addparam failed" % DXL2_ID)
#     quit()
#
# while 1:
#     print("Press any key to continue! (or press ESC to quit!)")
#     if getch() == chr(0x1b):
#         break
#
#     # Allocate goal position value into byte array
#     param_goal_position = [DXL_LOBYTE(DXL_LOWORD(dxl_goal_position[index])), DXL_HIBYTE(DXL_LOWORD(dxl_goal_position[index])), DXL_LOBYTE(DXL_HIWORD(dxl_goal_position[index])), DXL_HIBYTE(DXL_HIWORD(dxl_goal_position[index]))]
#
#     # Add Dynamixel#1 goal position value to the Bulkwrite parameter storage
#     dxl_addparam_result = groupBulkWrite.addParam(DXL1_ID, ADDR_GOAL_POSITION, LEN_GOAL_POSITION, param_goal_position)
#     if dxl_addparam_result != True:
#         print("[ID:%03d] groupBulkWrite addparam failed" % DXL1_ID)
#         quit()
#
#     # Add Dynamixel#2 LED value to the Bulkwrite parameter storage
#     dxl_addparam_result = groupBulkWrite.addParam(DXL2_ID, ADDR_LED_RED, LEN_LED_RED, [dxl_led_value[index]])
#     if dxl_addparam_result != True:
#         print("[ID:%03d] groupBulkWrite addparam failed" % DXL2_ID)
#         quit()
#
#     # Bulkwrite goal position and LED value
#     dxl_comm_result = groupBulkWrite.txPacket()
#     if dxl_comm_result != COMM_SUCCESS:
#         print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
#
#     # Clear bulkwrite parameter storage
#     groupBulkWrite.clearParam()
#
#     while 1:
#         # Bulkread present position and LED status
#         dxl_comm_result = groupBulkRead.txRxPacket()
#         if dxl_comm_result != COMM_SUCCESS:
#             print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
#
#         # Check if groupbulkread data of Dynamixel#1 is available
#         dxl_getdata_result = groupBulkRead.isAvailable(DXL1_ID, ADDR_PRESENT_POSITION, LEN_PRESENT_POSITION)
#         if dxl_getdata_result != True:
#             print("[ID:%03d] groupBulkRead getdata failed" % DXL1_ID)
#             quit()
#
#         # Check if groupbulkread data of Dynamixel#2 is available
#         dxl_getdata_result = groupBulkRead.isAvailable(DXL2_ID, ADDR_LED_RED, LEN_LED_RED)
#         if dxl_getdata_result != True:
#             print("[ID:%03d] groupBulkRead getdata failed" % DXL2_ID)
#             quit()
#
#         # Get present position value
#         dxl1_present_position = groupBulkRead.getData(DXL1_ID, ADDR_PRESENT_POSITION, LEN_PRESENT_POSITION)
#
#         # Get LED value
#         dxl2_led_value_read = groupBulkRead.getData(DXL2_ID, ADDR_LED_RED, LEN_LED_RED)
#
#         print("[ID:%03d] Present Position : %d \t [ID:%03d] LED Value: %d" % (DXL1_ID, dxl1_present_position, DXL2_ID, dxl2_led_value_read))
#
#         if not (abs(dxl_goal_position[index] - dxl1_present_position) > DXL_MOVING_STATUS_THRESHOLD):
#             break
#
#     # Change goal position
#     if index == 0:
#         index = 1
#     else:
#         index = 0
#
# # Clear bulkread parameter storage
# groupBulkRead.clearParam()

# # Disable Dynamixel#1 Torque
# dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)
# if dxl_comm_result != COMM_SUCCESS:
#     print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
# elif dxl_error != 0:
#     print("%s" % packetHandler.getRxPacketError(dxl_error))
#
# # Disable Dynamixel#2 Torque
# dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL2_ID, ADDR_TORQUE_ENABLE, TORQUE_DISABLE)
# if dxl_comm_result != COMM_SUCCESS:
#     print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
# elif dxl_error != 0:
#     print("%s" % packetHandler.getRxPacketError(dxl_error))

# Close port
# portHandler.closePort()