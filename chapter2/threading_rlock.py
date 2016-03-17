"""RLock example

Allow to release only for thread that is created the lock
"""

import threading
import time


class Box(object):

    lock = threading.RLock()

    def __init__(self):
        self.total_items = 0

    def execute(self, n):
        Box.lock.acquire()
        self.total_items += n
        Box.lock.release()

    def add(self):
        Box.lock.acquire()
        self.execute(1)
        Box.lock.release()

    def remove(self):
        Box.lock.acquire()
        self.execute(-1)
        Box.lock.release()


def adder(box, items):
    while items > 0:
        print('Adding 1 item to the box\n')
        box.add()
        time.sleep(5)
        items -= 1


def remover(box, items):
    while items > 0:
        print('Removing 1 item from the box\n')
        box.remove()
        time.sleep(5)
        items -= 1


if __name__ == '__main__':
    items = 5

    print('Putting', 5, 'items in the box')

    box = Box()

    t1 = threading.Thread(target=adder, args=(box, items))
    t2 = threading.Thread(target=remover, args=(box, items))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print(box.total_items, 'items still remain in the box')
