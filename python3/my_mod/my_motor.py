#! /usr/bin/env python
#coding: utf-8

import time
import Adafruit_PCA9685
import sys
sys.path.append("/2019_auv/my_mod")
# from my_state_write import state_write

pwm = Adafruit_PCA9685.PCA9685()
# pwm周波数設定
# pwm.set_pwm_freq(66)
# pwm.set_pwm_freq(500)
pwm.set_pwm_freq(1000)


# HAT-MDD10ピン設定
# ---------------
dc_xr_pwm = 7
dc_xr_dir = 13
# ---------------
# ドライバ負荷軽減
dc_xl_pwm = 12
dc_xl_dir = 6
# ---------------
dc_yr_pwm = 9
dc_yr_dir = 14
# ---------------
dc_yl_pwm = 10
dc_yl_dir = 5
# ---------------
dc_u_pwm = 11
dc_u_dir = 15
# ---------------
dc_d_pwm = 8
dc_d_dir = 4
# --------------------------------


#モータ1個の関数-------------------
#dc_xx_pwm モータ出力 0~4000
#dc_xx_dir 回転方向 0 or 4000

def dc_xr( val ):
    val, pone = my_map(val)
    pwm.set_pwm(dc_xr_pwm, 0, int(val))
    pwm.set_pwm(dc_xr_dir, 0, pone)

def dc_xl( val ):
    val, pone = my_map(val)
    pwm.set_pwm(dc_xl_pwm, 0, int(val))
    pwm.set_pwm(dc_xl_dir, 0, pone)

def dc_yr( val ):
    val, pone = my_map(val)
    pwm.set_pwm(dc_yr_pwm, 0, int(val))
    pwm.set_pwm(dc_yr_dir, 0, pone)

def dc_yl( val ):
    val, pone = my_map(val)
    pwm.set_pwm(dc_yl_pwm, 0, int(val))
    pwm.set_pwm(dc_yl_dir, 0, pone)

def dc_u( val ):
    motor_vals("dc_u", val)
    val, pone = my_map(val)
    pwm.set_pwm(dc_u_pwm, 0, val)
    pwm.set_pwm(dc_u_dir, 0, pone)

def dc_d( val ):
    motor_vals("dc_d", val)
    val, pone = my_map(val)
    pwm.set_pwm(dc_d_pwm, 0, val)
    pwm.set_pwm(dc_d_dir, 0, pone)

#モータ1個の関数-------------------


#進行-----------------------------

# 前進_後進(go_back)
def go_back( val ):
    dc_xl(val)
    dc_xr(-val)

# 前進_後進(それぞれの出力を指定）
def go_back_each(l, r):
    dc_xl(l)
    dc_xr(-r)

# 上昇_下降(up_down)
def up_down( val ):
    dc_yl(val)
    dc_yr(-val)

# 上昇_下降(それぞれの出力を指定)
def up_down_each( l, r ):
    dc_yl(l)
    dc_yr(-r)

# 右回り_左回り(spinturn)
def spinturn( val ):
    dc_xl(val)
    dc_xr(val)

# 右回り_左回り(それぞれの出力を指定)
def spinturn_each( l, r ):
    dc_xl(l)
    dc_xr(-r)

# 右傾き_左傾き
def roll( val ):
    dc_yl(val)
    dc_yr(val)

#進行-----------------------------


#停止-----------------------------

def stop():
    # print"\nSTOP"
    pwm.set_pwm(dc_xr_pwm, 0, 0)
    pwm.set_pwm(dc_xl_pwm, 0, 0)
    pwm.set_pwm(dc_yr_pwm, 0, 0)
    pwm.set_pwm(dc_yl_pwm, 0, 0)

def stop_go_back():
    # print"\nSTOP_GO_BACK"
    pwm.set_pwm(dc_xr_pwm, 0, 0)
    pwm.set_pwm(dc_xl_pwm, 0, 0)

def stop_up_down():
    # print"\nSTOP_UP_DOWN"
    pwm.set_pwm(dc_yr_pwm, 0, 0)
    pwm.set_pwm(dc_yl_pwm, 0, 0)

#停止-----------------------------


#値変換関数------------------------

def my_map(val):
    if val == 0:
        val = 0
        pone = 1
    elif val >= 0:
        pone = 4000
        in_min = 0
        in_max = 100
        out_min = 0
        out_max = 4000
        val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    else:
        pone = 1
        in_min = 0
        in_max = -100
        out_min = 0
        out_max = 4000
        val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    return val, pone

#値変換関数------------------------


if __name__ == '__main__':
    while True:
        try:
            spinturn(30)
        except KeyboardInterrupt as e:
            stop()
            break
