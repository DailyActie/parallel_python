"""Thread synchronisation with semaphores"""

import threading
import time
import random

semaphore = threading.Semaphore(0)


def consumer():
    print('Consumer is waiting')
    semaphore.acquire()
    print('Consumer notify : consumed item number', item)


def producer():
    global item
    time.sleep(10)
    item = random.randint(0, 1000)
    print('Producer notify : produced item number', item)
    semaphore.release()


if __name__ == '__main__':
    for i in range(5):
        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

    print('Program terminated')
