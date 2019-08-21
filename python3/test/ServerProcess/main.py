import time
from multiprocessing import Manager, Process
from sirial import sirial_process

def log_process(data):
    with open('/2019_auv/test/ServerProcess/log.txt', 'w') as f:
        while True:
            f.writelines(str(data.value) + "\n")
            print("log_process")
            time.sleep(0.1)

def blance_process(data, blance):
    while True:
        blance.value = data.value * 2
        print("blance_process:",blance.value)
        time.sleep(0.2)

def my_moter(blance):
    output = 30 - blance.value
    print("my_moter",output)

if __name__ == "__main__":
        with Manager() as manager:
            data = manager.Value('d', 0.0)
            blance = manager.Value('i', 0)

            process1 = Process(target=sirial_process, args=[data])
            process2 = Process(target=log_process, args=[data])
            process3 = Process(target=blance_process, args=[data, blance])

            process1.start()
            process2.start()
            process3.start()

            while True:
                my_moter(blance)
                time.sleep(0.2)
                print("\nmain--------")
                print(data.value)
                print("main--------\n")

            process1.join()
            process2.join()
            process3.join()

            print("main Process end")