# -*- coding: utf-8 -*-
# sudo pip install pyserial
import serial
import ast
import time
from datetime import datetime

import sys
sys.path.append("/kaiyo/my_mod")
# from my_tinydb import insert, select, purge

# ArduinoMEGAとpinで接続
ser = serial.Serial('/dev/ttyS0', 115200)
# ArduinoMEGAとUSBケーブル接続
# ser = serial.Serial('/dev/ttyACM0', 115200)


def get_data(val):
    while True:
        # Arduino から一行取得
        data = ser.readline()
        # 受信エラー確認
        try:
            # dictに変換
            data = ast.literal_eval(data)
            # print data

            if val == "all":
                # yawの値を変換してから渡す
                # 0 ~ 180, 0 ~ -180
                data["yaw"] = my_map(data["yaw"])
                # print "bbb", data["yaw"]
                return data
            if val == "yaw": return my_map(data[val])
            if val == "compass": return my_map(data[val])
            if val == "yaw2": return data["yaw"]
            if val == "state": return data["state"]
            if val == "average_rot0_rot1": return (data["rot0"] + data["rot1"]) / 2
            if val == "average_rot2_rot3": return (data["rot2"] + data["rot3"]) / 2
            return data[val]
        except SyntaxError:
            # 受信エラー
            print "Reception Error!!"



# ArduinoMEGAにコマンド送信
def send_data(val):
    ser.write(val)


"""
# yawの値変換
def my_map(val):
    in_min = 0
    in_max = 360
    out_min = 0
    out_max = 100
    val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    # 少数切り捨ての為intに変換
    return int(val)
"""

# yawの値が「右に-1~-180, 左に1~180」
def my_map(val):
    if val <= 0:
        in_min = -1
        in_max = -180
        out_min = 0
        out_max = 50
        val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        # 少数切り捨ての為intに変換
        return int(val)
    else:
        in_min = 1
        in_max = 180
        out_min = 100
        out_max = 50
        val = (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
        # 少数切り捨ての為intに変換
        return int(val)


if __name__ == '__main__':
    send_data("reboot")
    while True:
        # print type(get_data("all"))
        print get_data("all")

# ser.close()
