#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
import gps
import ast
import time

# GPSのデータを取得して還す--------------------------------------------

def get_gps_data():
    session = gps.gps("localhost", "2947")
    session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
    lat = ""
    lon = ""
    alt = ""
    while True:
        try:
            # gps データ取得
            report = next(session)
            # print report # To see all report data, uncomment the line below
            if report['class'] == 'TPV':
                if hasattr(report, 'lat'):
                    lat = float(report.lat)
                if hasattr(report, 'lon'):
                    lon = float(report.lon)
                if hasattr(report, 'alt'):
                    alt = float(report.alt)
                if( lat!=""and lon!="" and alt!="" ):
                    gps_data_dict = {"lat":lat, "lng":lon, "alt":alt}
                    # str に変換
                    gps_data_dict["datetime"] = str(datetime.now())
                    # print gps_data_dict
                    return gps_data_dict
        except KeyError:
            pass
        except KeyboardInterrupt:
            quit()
        except StopIteration:
            session = None
            print("GPSD has terminated!!")

# GPSのデータを取得して還す--------------------------------------------


if __name__ == '__main__':
    # gps_sensor_join_data()

    print(get_gps_data())

    # gps_data_logging()
