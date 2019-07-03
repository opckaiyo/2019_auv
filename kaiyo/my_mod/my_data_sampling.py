# -*- coding: utf-8 -*-
# sudo pip install pyserial
import serial
import ast
import time
from datetime import datetime
import sys
sys.path.append("/kaiyo/my_mod")
# from my_get_serial import get_data
# -----------------------------------------------------------------------------

# ArduinoMEGAとpinで接続
# ser = serial.Serial('/dev/ttyS0', 115200)
# ArduinoMEGAとUSBケーブル接続
ser = serial.Serial('/dev/ttyACM0', 115200)


# -----------------------------------------------------------------------------

def data_sampling(set_sample_rate=0.2):
    # logsをテキストに残すか聞くプログラム
    sensor_log_file_time = open('/kaiyo/log/sensor_log/sensor_log_'+str(datetime.now().strftime('%Y%m%d_%H%M%S'))+'.txt', 'a')
    sensor_log_file = open('/kaiyo/log/sensor_log/sensor_log.txt', 'w')

    start_time = time.time()
    while True:
        # Arduino から一行取得
        data = ser.readline()
        try:
            # dictに変換
            data = ast.literal_eval(data)
            # print data["flw0"],
            # print data["flw1"],
            # print data["flw2"]
            # print data

            # サンプリングレート以上時間が経過したら書き込み
            ela_time = time.time() - start_time
            if ela_time >= set_sample_rate:
                data["datetime"] = str(datetime.now())

                sensor_log_file_time.writelines(str(data) + "\n")
                sensor_log_file.writelines(str(data) + "\n")

                start_time = time.time()

        except SyntaxError:
            # 受信エラー
            print "Reception Error!!"
            # pass


# -----------------------------------------------------------------------------

if __name__ == '__main__':
    while True:
        try:
            data_sampling(set_sample_rate=0.2)
        except KeyboardInterrupt as e:
            quit()
            # pass
            # print "\nFile close!!\n"
            # sensor_log_file_time.close()
            # sensor_log_file.close()
