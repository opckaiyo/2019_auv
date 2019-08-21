import time
from multiprocessing import Manager, Process

def sirial_process(data):
        while True:
                data.value += 0.5
                print("process sirial:",data.value)
                time.sleep(0.2)