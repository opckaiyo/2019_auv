#coding: utf-8
# 時間制御を行うライブラリ
import time
# 自作関数をインポートするためのライブラリ
import sys
# 並列処理に必要な関数
from multiprocessing import Manager, Process
# シリアル通信に必要な関数
import serial
# データ整形に必要
import ast

# 自作関数のインポート
sys.path.append("/2019_auv/my_mod")
# ArduinoMegaとシリアル通信してセンサデータをもらう関数
from my_get_serial import get_data, send_data
# PCA9685と通信しモータを制御する関数
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, go_back_each, up_down_each, spinturn_each
# 主にロボットの姿勢制御（方向、深度）を行う関数
from my_balance import go_yaw, roteto, go_depth
# プロポ（t19j）を使って、ロボットを制御するための関数
from my_rc import t10j, t10j_time, t10j_mode_sumo
# プログラムスタート時にロボットの状態や初期設定の動作を行う関数
from my_check import operation_check, battery_check, my_exit, first_action
# 7色LEDの制御を行う関数
from my_gpio import led_red, led_green, led_yellow, led_off, led_blue, led_purple, led_lihtblue
# 大会コースに沿った動作を行う関数。（主にこの関数の値を調整して大会挑んだ）
from my_course import course_convention, course_pool
# プログラムがエラーを発生したときにエラーの内容をテキストファイルに記録する関数
from my_text_write import error_log_write
# GPSデータの取得
from my_gps import get_gps_data
# GPSによるウェイポイント制御を行う関数
from my_waypoint import get_direction_distance

# ArduinoMEGAとpinで接続---------
ser = serial.Serial('/dev/ttyS0', 115200)
# ArduinoMEGAとpinで接続---------

#　サブプロセス終了のための関数---------------------------------------

def sebprocess_kill():
    process1.terminate()
    process2.terminate()
    process3.terminate()

#　サブプロセス終了のための関数---------------------------------------

# この関数にメインのプログラムを記述する-------------------------------

def my_main():
    go_back(15)
    print("\n\n")
    print("yaw_MV", yaw_MV.value, "\n")
    print("depth_MV", depth_MV.value, "\n")

# この関数にメインのプログラムを記述する-------------------------------

if __name__ == "__main__":
    try:
        with Manager() as manager:
            data = manager.dict()
            yaw_MV = manager.Value("d", 0.0)
            depth_MV = manager.Value("d", 0.0)
            goal_yaw = manager.Value("i", 0)
            goal_depth = manager.Value("i", 0)

            val = ser.readline()
            val = ast.literal_eval(val.decode('unicode-escape'))
            for i in val:
                data[i] = val[i]

            process1 = Process(target=get_data, args=[data])
            process2 = Process(target=go_yaw, args=[goal_yaw,data,yaw_MV])
            process3 = Process(target=go_depth, args=[goal_depth,data,depth_MV])

            process1.start()
            process2.start()
            process3.start()

            first_action(data)

            while True:
                my_main()

        process1.join()
        process2.join()
        process3.join()

    except Exception as e:
        sebprocess_kill()
        print("\n------")
        print("main.py : ",e)
        print("------\n")
        my_exit()

    except KeyboardInterrupt as key:
        sebprocess_kill()
        print("\n------")
        print("main.py : ",key)
        print("------\n")
        my_exit()

    else:
        sebprocess_kill()
        print("\n------")
        print("main.py : else")
        print("------\n")
        my_exit()
