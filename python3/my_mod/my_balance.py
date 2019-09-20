#coding: utf-8
import numpy as np
import time
import sys
sys.path.append("/2019_auv/my_mod")
from multiprocessing import Manager, Process
from my_get_serial import get_data, send_data
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, go_back_each, up_down_each, spinturn_each


#PID制御で角度調整---------------------------------------------------------------

# M : 与える操作量
# M1 : 一つ前に与えた操作量
# goal : 目的値
# e : 偏差(目的値と現在値の差)
# e1 : 前回に与えた偏差
# e2 : 前々回に与えた偏差
# Kp : 比例制御（P制御)の比例定数
# Ki : 積分制御（I制御)の比例定数
# Kd : 微分制御（D制御)の比例定数

def go_yaw(goal_yaw,data,yaw_MV):
    while True:
        M = 0.00
        M1 = 0.00

        e = 0.00
        e1 = 0.00
        e2 = 0.00

        Kp = 0.001
        Ki = 0.01
        Kd = 0.5

        now_yaw = data["yaw"]

        if now_yaw < 0:
            now_yaw = 360 + now_yaw

        if goal_yaw.value < 0:
            goal_yaw.value = 360 + goal_yaw.value

        while True:

            now_yaw = data["yaw"]

            M1 = M
            e1 = e
            e2 = e1

            if now_yaw < 0:
                now_yaw = 360 + now_yaw

            if abs(goal_yaw.value - now_yaw) > 180:
                e = 360 - abs(goal_yaw.value - now_yaw)
            else:
                e = abs(goal_yaw.value - now_yaw)

            M = M1 + Kp * (e-e1) + Ki * e + Kd * ((e-e1) - (e1-e2))
            direction = roteto(now_yaw,goal_yaw)

            if M > 30:
                M = 30
            elif M < 10:
                M = 10

            if goal_yaw.value != 0:
                if now_yaw - 1 < goal_yaw.value < now_yaw + 1:
                    yaw_MV.value = 0
                    break
            else:
                if now_yaw > 359 or now_yaw < 1:
                    yaw_MV.value = 0
                    break

            yaw_MV.value = M * direction

    stop()


#左周りが近いなら-1右周りなら1を返す
def roteto(yaw,goal):
    direction = 0
    if yaw <= 180:
        if 0 > yaw - goal.value > -180:
            direction = -1
        else:
            direction = 1
    elif yaw <= 360:
        if 0 < yaw - goal.value < 180:
            direction = 1
        else:
            direction = -1

    return direction

#PID制御で角度調整---------------------------------------------------------------


#PID制御で水深調整---------------------------------------------------------------

def go_depth(goal_depth,data,yaw_depth):
    while True:
        M = 1.00
        M1 = 0.00

        e = 0.00
        e1 = 0.00
        e2 = 0.00

        Kp = 0.10
        Ki = 0.10
        Kd = 0.10

        now_depth = data("depth")

        while(now_depth - 0.4 < now_depth < now_depth + 0.4):
            M1 = M
            e1 = e
            e2 = e1
            e = goal_depth - now_depth

            M = M1 + Kp * (e-e1) + Ki * e + Kd * ((e-e1) - (e1-e2))

            if goal_depth < now_depth:
                direction = 1
            else:
                direction = -1

            if M > 30:
                M = 30
            elif M < 10:
                m = 10

            up_down(M * direction)
            time.sleep(0.2)

    stop()

#PID制御で水深調整---------------------------------------------------------------

if __name__ == '__main__':
    send_data("reboot")
    while True:
        try:
            t1 = time.time()
            go_yaw(180)
            t2 = time.time()
            print("time : ",t2 - t1)
        except KeyboardInterrupt as e:
            stop()
            break
