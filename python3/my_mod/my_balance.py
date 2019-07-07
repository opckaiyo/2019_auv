#coding: utf-8
import numpy as np
import time
import sys
sys.path.append("/2019_auv/my_mod")
from my_get_serial import get_data, send_data
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, go_back_each, up_down_each, spinturn_each


#PID制御で角度調整---------------------------------------------------------------

def go_yaw(goal):
    M = 1.00
    M1 = 0.00

    e = 0.00
    e1 = 0.00
    e2 = 0.00

    Kp = 0.10
    Ki = 0.10
    Kd = 0.10

    now_yaw = get_data("yaw")

    while(now_yaw - 1 < now_yaw < now_yaw + 1):
        M1 = M
        e1 = e
        e2 = e1
        e = goal - now_yaw

        M = M1 + Kp * (e-e1) + Ki * e + Kd * ((e-e1) - (e1-e2))
        direction = roteto(now_yaw,goal)
        spinturn(30 * direction)
        time.sleep(M)
        stop()

#左周りが近いなら-1右周りなら1を返す
def roteto(yaw,goal):
    direction = 0
    if yaw <= 180:
        if 0 > yaw - goal > -180:
            direction = -1
        else:
            direction = 1
    elif yaw <= 360:
        if 0 < yaw - goal < 180:
            direction = 1
        else:
            direction = -1

    return direction

#PID制御で角度調整---------------------------------------------------------------


#PID制御で水深調整---------------------------------------------------------------

def go_depth(goal):
    M = 1.00
    M1 = 0.00

    e = 0.00
    e1 = 0.00
    e2 = 0.00

    Kp = 0.10
    Ki = 0.10
    Kd = 0.10

    now_depth = get_data("depth")

    while(now_depth - 0.4 < now_depth < now_depth + 0.4):
        M1 = M
        e1 = e
        e2 = e1
        e = goal - now_depth

        M = M1 + Kp * (e-e1) + Ki * e + Kd * ((e-e1) - (e1-e2))
        if goal < now_depth:
            direction = 1
        else:
            direction = -1

        up_down(30 * direction)
        time.sleep(abs(M))
        stop()

#PID制御で水深調整---------------------------------------------------------------

if __name__ == '__main__':
    pass
