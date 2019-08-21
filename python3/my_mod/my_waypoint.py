#coding: utf-8
import math
import time
import ast

import sys
sys.path.append("/2019_auv/my_mod")
from my_gps import get_gps_data
from my_balance import go_yaw, go_depth
from my_check import operation_check, battery_check, my_exit, first_action
from my_motor import go_back, up_down, spinturn, roll, stop, stop_go_back, stop_up_down, go_back_each, up_down_each, spinturn_each
from my_gpio import led_red, led_green, led_yellow, led_off, led_blue, led_purple, led_lihtblue


# -----------------------------------------------------------------------------

# pgsで現在地を取得して目標地点までの角度と距離を計算
def get_direction_distance(goal_lat, goal_lng):
    # gpsで現在地を取得
    now_gps_data = get_gps_data()
    now_lat = now_gps_data["lat"]
    now_lng = now_gps_data["lng"]

    print(("now_lat  :", now_lat))
    print(("now_lng  :", now_lng))
    print(("goal_lat :", goal_lat))
    print(("goal_lng :", goal_lng))

    print("now_lat  :", now_lat)
    print("now_lng  :", now_lng)
    print("goal_lat :", goal_lat)
    print("goal_lng :", goal_lng)

    lat_length = goal_lat - now_lat
    lng_length = goal_lng - now_lng

    # 方位を計算
    #direction = math.atan2(lat_length, lng_length) / 0.01745329
    direction = math.degrees(math.atan2(lat_length, lng_length))
    #9dセンサの出力は正面が0度だが計算上はそこからccwに90度ずれた場所が0度なので90度そらしている
    direction -= 90

    # 距離を計算
    lat_distance = lat_length * 111263.283
    lng_distance = lng_length * 111263.283
    distance = math.sqrt((lng_distance * lng_distance) + (lat_distance * lat_distance))

    # 回転数を計算（30回転で1m）
    set_rot = int(distance * 30)

    goal_gps_data = {"direction":int(direction), "distance":int(distance), "set_rot":set_rot}
    print(goal_gps_data)

    return goal_gps_data


# -------------------------------------------------------------------

if __name__ == '__main__':
    try:
        pad_rc_route_data_creation()
        # test()
        my_exit()
    except KeyboardInterrupt as e:
        my_exit()
