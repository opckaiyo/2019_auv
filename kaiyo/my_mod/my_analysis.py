# -*- coding: utf-8 -*-
import ast
from time import sleep

import sys
sys.path.append("/kaiyo/my_mod")

#------------------------------------------------------------------------------


def get_log():
    vals_min = {}
    vals_max = {}
    vals = {}
    cnt = 0
    print "Please file name :",
    file_name = raw_input()

    # file_name = "/kaiyo/log/log_181109_112516.txt"
    file = open(file_name, 'r')
    data = file.readline()
    data = ast.literal_eval(data)

    print "\n----------------------------"
    print "File name :", file_name
    print "keys :",
    for key in data.keys():
        print key,
        vals_min[key] = 0
        vals_max[key] = 0
    print "\n----------------------------\n"
    file.close()
    # sleep(2)
    for key, val in vals_min.items():
        file = open(file_name, 'r')
        a = -1000
        while True:
            try:
                data = file.readline()
                data = ast.literal_eval(data)

                vals[str(cnt)] = data[key]

                # 最大値を求める
                if a <= data[key]:
                    a = data[key]

                cnt+=1
            except Exception as e:
                print key
                print "----------------------------"
                print "MIN :", min(vals.values())
                print "MAX :", max(vals.values())
                print "----------------------------\n"

                vals_min[key] = min(vals.values())
                # vals_max[key] = max(vals.values())
                vals_max[key] = a
                file.close()
                break

    print "ALL"
    print "----------------------------"
    print "Number of data :", cnt/len(vals_min)
    # print "MIN :", vals_min
    # print "MAX :", vals_max
    print "----------------------------"
    print "MIN"
    for key, val in sorted(vals_min.items()):
        print key+"\t\t", val
    print "----------------------------"
    print "MAX"
    for key, val in sorted(vals_max.items()):
        print key+"\t\t", val
    print "----------------------------\n"


if __name__ == '__main__':
    # get_log("roll")
    get_log()
