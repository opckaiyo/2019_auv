#coding: utf-8
# 時間制御を行うライブラリ
import time
# 自作関数をインポートするためのライブラリ
import sys

# 自作関数のインポート
sys.path.append("/2019_kaiyo_ver1/my_mod")
# ArduinoMegaとシリアル通信してセンサデータをもらう関数
from my_get_serial import get_data, send_data
# PCA9685と通信しモータを制御する関数
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, go_back_each, up_down_each, spinturn_each
# 主にロボットの姿勢制御（方向、深度）を行う関数
from my_balance import
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
# GPSデータの取得や、GPSデータをテキストファイルに保存する関数
from my_gps import gps_sensor_join_data
# GPSによるウェイポイント制御を行う関数
from my_waypoint import waypoint, pad_rc_route_data_creation
# 水中ロボット班から借りたゲームパッドでラジコン制御するとに使う関数
from my_gamepad import pad_rc

# -----------------------------------------------------------------------------

# この関数にメインのプログラムを記述する
def my_main():
    # センサーデータ取得
    data = get_data("all")
    # センサデータ表示
    # print data





# -------------------------------------------------------------------


if __name__ == '__main__':
    try:
        # モードなどの設定
        first_action()

        while True:
            # 予期せぬエラーが発生した時の処理
            try:
                # Ctrl-cを押したときの処理
                try:
                    # メインのプログラム
                    # ----------------------------------------
                    my_main()
                    # my_exit()
                    # break
                    # ----------------------------------------
                except KeyboardInterrupt as e:
                    # Ctrl-cを押したときの処理
                    print "\nCtrl-c!!"
                    # プログラムを終了したらデータを作成
                    gps_sensor_join_data()
                    # print e
                    my_exit()
            except Exception as e:
                # 予期せぬエラーが発生した時の処理
                stop()
                # エラーの内容を残す
                error_log_write(e)
                print "\nError =",e
                print "Error!!!!!!!!!!!!!!!!!!!!!!!"
                for i in range(20):
                    led_green()
                    time.sleep(0.05)
                    led_off()
                    time.sleep(0.05)
                # my_exit()

    except KeyboardInterrupt as e:
        print "\nCtrl-c!!"
        # プログラムを終了するときの処理
        my_exit()
