# -*- coding: utf-8 -*-
# sudo pip install pyserial
# 並列処理に必要な関数
from multiprocessing import Manager, Process
import types
import serial
import ast
import time
from datetime import datetime
import sys
sys.path.append("/2019_auv/my_mod")
# from my_tinydb import insert, select, purge

# ArduinoMEGAとpinで接続
ser = serial.Serial('/dev/ttyS0', 115200)
# ArduinoMEGAとUSBケーブル接続
# ser = serial.Serial('/dev/ttyACM0', 115200)

#指定させてデータを返す変数---------------------------------------------
"""
def get_data(val):
    # Arduino から一行取得
    data = ser.readline()
    # 受信エラー確認
    try:
        # dictに変換
        data = ast.literal_eval(data.decode('unicode-escape'))

        if val == "all": return data
        # print data

        return data[val]
    except SyntaxError:
        # 受信エラー
        print("Reception Error!!")
"""
def get_data(data):
    while True:
        # Arduino から一行取得
        val = ser.readline()
        # 受信エラー確認
        try:
            # dictに変換
            val = ast.literal_eval(val.decode('unicode-escape'))
            for i in val:
                data[i] = val[i]

        except SyntaxError:
            # 受信エラー
            print("Reception Error!!")

#指定させてデータを返す変数---------------------------------------------


#ArduinoMEGAにコマンド送信---------------------------------------------

#("  'run':'シリアル通信を開始する。', ");
#("  'stop':'シリアル通信を停止する。', ");
#("  'reboot':'Arduinoを再起動する。', ");
#("  'reset xxx':'curまたはrotの値をリセットする。', ");
#("  'debug':'デバッグモードに移行offをつけると通常モードに戻る。', ");
#("  'time XXXX':'無限ループ時の待機時間をXXXXミリ秒にする。', ");
#("  'yaw_zero off':'yawの初期リセット値を無効化', ");
#("  'remove error':'状態を確認し問題なかったらstateをnormalにする', ");

#主に通信開始時に動機をとるために再起動する val = reboot

def send_data(val):
    ser.write(val.encode('unicode-escape'))

#ArduinoMEGAにコマンド送信---------------------------------------------


if __name__ == '__main__':
    send_data("reboot")
    while True:
        # print type(get_data("all"))
        print((get_data("all")))

# ser.close()
