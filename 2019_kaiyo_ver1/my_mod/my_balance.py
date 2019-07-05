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
        spinturn(30)
        time.sleep(M)
        stop()

def roteto(yaw,goal):
    if now_yaw >= 0:



#PID制御で角度調整---------------------------------------------------------------


#PID制御で水深調整---------------------------------------------------------------



#PID制御で水深調整---------------------------------------------------------------

if __name__ == '__main__':
    pass
