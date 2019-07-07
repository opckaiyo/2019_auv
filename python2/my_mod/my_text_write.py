# coding:utf8
from datetime import datetime


def error_log_write(state):
    #日付ごとにファイルを作成
    file = open('/2019_auv/log/error_log/error_log_'+str(datetime.now().strftime('%Y%m%d'))+'.txt', 'a')
    file.writelines(str(state) + " : " + str(datetime.now()) + "\n")
    file.close()



if __name__ == '__main__':
    state_write("浮上")
