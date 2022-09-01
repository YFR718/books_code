import os
import time
from multiprocessing import Pool


def task(name):
    print("正在执行：", os.getpid(), name)
    time.sleep(1)


if __name__ == '__main__':
    p = Pool(3)
    for i in range(10):
        p.apply_async(task, args=(i,))
    p.close()
    p.join()  # 等待子进程结束
