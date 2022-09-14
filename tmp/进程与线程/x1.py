import threading, time


def process():
    for i in range(3):
        time.sleep(1)
        print(threading.current_thread().name)


if __name__ == '__main__':
    threads = [threading.Thread(target=process) for i in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print("over")
