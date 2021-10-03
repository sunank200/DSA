import threading
import time
from threading import Thread


def thrdFunc():
    print("Starting of thread function.")
    time.sleep(5)
    print("Thread function completed.")


# thrdFunc()
print(threading.activeCount())
thrd = Thread(target=thrdFunc)

thrd.start()
print(threading.activeCount())
thrd.join()  # wait for thread to completed
print(threading.activeCount())

# Global interpreter lock (GIL) : Due to , only one thread can execute the
# code at once (even though certain performance-oriented libraries overcome
# this limitation)

kill_thread = False


def working_thread():
    while True:
        if kill_thread == True:
            return


thrd_run = Thread(target=working_thread())
print(threading.activeCount())

thrd_run.start()

# lets create multiple threads
thrd_1 = Thread(target=working_thread())
thrd_2 = Thread(target=working_thread())

thrd_1.start()
thrd_2.start()
print(threading.activeCount())


# CPU usage is just 100% for all threads

# for multiple threads - use multiprocessing not multithreading in python

import multiprocessing as mp
from multiprocessing import Process


def working_process():
    while True:
        pass


proc = Process(working_process())
proc.start()
proc.terminate()

# object oriented threads


class MyThread(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print("A thread is running.")
        time.sleep(5)
        print("A thread is exiting.")


m = MyThread()
m.start()
m.join()
