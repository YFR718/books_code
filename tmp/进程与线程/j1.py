from multiprocessing import Process


def test(interval):
    print("testing!!!")


if __name__ == '__main__':
    p = Process(target=test, args=(1,))
    p.start()
