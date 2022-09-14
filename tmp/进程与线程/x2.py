import threading
import time

nums = 0
mutex = threading.Lock()
class SubThread(threading.Thread):
    def run(self):
        global nums
        for i in range(10000000):
            mutex.acquire()
            nums+=1
            mutex.release()


if __name__ == '__main__':

    t1 = SubThread()
    t2 = SubThread()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("over",nums)