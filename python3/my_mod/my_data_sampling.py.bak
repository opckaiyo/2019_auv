# -*- coding: utf-8 -*-
# sudo pip install pyserial
import serial
import ast
import time
from datetime import datetime
import sys
import gps
import os
import ConfigParser
import distutils.util

from my_get_serial import get_data

sys.path.append("/2019_auv/my_mod")

#設定ファイル読み込み
inifile = ConfigParser.SafeConfigParser()
inifile.read('/2019_auv/my_config/my_config.ini')
set_sensor_log =        distutils.util.strtobool(inifile.get('set_mode', 'set_sensor_log'))
set_gps_log =           distutils.util.strtobool(inifile.get('set_mode', 'set_gps_log'))
set_sensor_gps_log =    distutils.util.strtobool(inifile.get('set_mode', 'set_sensor_gps_log'))

# from my_get_serial import get_data
# -----------------------------------------------------------------------------

# ArduinoMEGAとpinで接続
# ser = serial.Serial('/dev/ttyS0', 115200)
# ArduinoMEGAとUSBケーブル接続
#ser = serial.Serial('/dev/ttyACM0', 115200)


# -----------------------------------------------------------------------------

def data_sampling(set_sample_rate=0.2):
    # logsをテキストに残すか聞くプログラム
    try:
        os.makedirs('/2019_auv/log/sensor_log/'+str(datetime.now().strftime('%Y%m%d')))
    except FileExistsError:
        pass
    sensor_log_file_time = open('/2019_auv/log/sensor_log/'+str(datetime.now().strftime('%Y%m%d'))+'/sensor_log_'+str(datetime.now().strftime('%Y%m%d_%H%M%S'))+'.txt', 'a')

    start_time = time.time()
    while True:
        # Arduino から一行取得
        data = get_data("all")
        try:
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

def gps_data_logging():
    # log ファイル生成
    try:
        os.makedirs('/2019_auv/log/gps_log/'+str(datetime.now().strftime('%Y%m%d')))
    except FileExistsError:
        pass
    gps_log_file_time = open('/kaiyo/log/gps_log/'+str(datetime.now().strftime('%Y%m%d'))+'/gps_log_'+str(datetime.now().strftime('%Y%m%d_%H%M%S'))+'.txt', 'a')

    session = gps.gps("localhost", "2947")
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
    lat = ""
    lon = ""
    alt = ""

    while True:
        try:
            # gps データ取得
            report = session.next()
            # print report # To see all report data, uncomment the line below
            if report['class'] == 'TPV':
                if hasattr(report, 'lat'):
                    lat = float(report.lat)
                if hasattr(report, 'lon'):
                    lon = float(report.lon)
                if hasattr(report, 'alt'):
                    alt = float(report.alt)
                if( lat!=""and lon!="" and alt!="" ):
                    # 2秒間待つ
                    time.sleep(2)

                    gps_data_dict = {"lat":lat, "lng":lon, "alt":alt}
                    # str に変換
                    gps_data_dict["datetime"] = str(datetime.now())
                    # log に書き込み
                    gps_log_file_time.writelines(str(gps_data_dict) + "\n")
                    gps_log_file.writelines(str(gps_data_dict) + "\n")

        except KeyError:
                pass
        except KeyboardInterrupt:
            quit()
        except StopIteration:
            session = None
            print "GPSD has terminated!!"

def sensor_gps_log(set_sample_rate=0.2):

    try:
        os.makedirs('/2019_auv/log/sensor_log/'+str(datetime.now().strftime('%Y%m%d')))
    except FileExistsError:
        pass

    try:
        os.makedirs('/2019_auv/log/gps_log/'+str(datetime.now().strftime('%Y%m%d')))
    except FileExistsError:
        pass

    try:
        os.makedirs('/2019_auv/log/join_log/'+str(datetime.now().strftime('%Y%m%d')))
    except FileExistsError:
        pass

    if set_sensor_log: sensor_log_file_time = open('/2019_auv/log/sensor_log/'+str(datetime.now().strftime('%Y%m%d'))+'/sensor_log_'+str(datetime.now().strftime('%Y%m%d_%H%M%S'))+'.txt', 'a')
    if set_gps_log: gps_log_file_time = open('/2019_auv/log/gps_log/'+str(datetime.now().strftime('%Y%m%d'))+'/gps_log_'+str(datetime.now().strftime('%Y%m%d_%H%M%S'))+'.txt', 'a')
    if set_sensor_gps_log: gps_sensor_log_file_time = open('/2019_auv/log/join_log/'+str(datetime.now().strftime('%Y%m%d'))+'/gps_sensor_log_'+str(datetime.now().strftime('%Y%m%d_%H%M%S'))+'.txt', 'a')

    start_time = time.time()

    session = gps.gps("localhost", "2947")
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
    lat = ""
    lon = ""
    alt = ""

    while True:
        # Arduino から一行取得
        data = get_data("all")
        try:
            # サンプリングレート以上時間が経過したら書き込み
            ela_time = time.time() - start_time
            if ela_time >= set_sample_rate:

                i = 0

                #sensor--------------------------------------

                data["datetime"] = str(datetime.now())

                if set_sensor_log: sensor_log_file_time.writelines(str(data) + "\n")

                #sensor--------------------------------------


                #gps-----------------------------------------

                report = session.next()
                # print report # To see all report data, uncomment the line below
                if report['class'] == 'TPV':
                    if hasattr(report, 'lat'):
                        lat = float(report.lat)
                    if hasattr(report, 'lon'):
                        lon = float(report.lon)
                    if hasattr(report, 'alt'):
                        alt = float(report.alt)
                    if i >= 10:
                        i = 0
                        if( lat!=""and lon!="" and alt!="" ):
                            gps_data_dict = {"lat":lat, "lng":lon, "alt":alt}
                            # str に変換
                            gps_data_dict["datetime"] = str(datetime.now())
                            # log に書き込み
                            if set_gps_log: gps_log_file_time.writelines(str(gps_data_dict) + "\n")
                    else:
                        i += 1

                #gps-----------------------------------------


                #join----------------------------------------

                data["lat"] = lat
                data["lon"] = lon
                data["alt"] = alt

                if set_sensor_gps_log: gps_sensor_log_file_time.writelines(str(data) + "\n")

                #join----------------------------------------

                start_time = time.time()

        except SyntaxError:
            # 受信エラー
            print "Reception Error!!"
        except KeyError:
                pass
        except KeyboardInterrupt:
            quit()
        except StopIteration:
            session = None
            print "GPSD has terminated!!"

# -----------------------------------------------------------------------------

if __name__ == '__main__':
    while True:
        try:
            sensor_gps_log(set_sample_rate=0.2)
        except KeyboardInterrupt as e:
            quit()
            # pass
            # print "\nFile close!!\n"
            # sensor_log_file_time.close()
            # sensor_log_file.close()
