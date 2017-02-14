# coding=utf-8

"""How to determine the current thread?"""

import threading
import time
import logging

logging.basicConfig(level=logging.INFO)


def first_function():
    logging.info(threading.currentThread().getName() + str(' is starting...'))
    time.sleep(2)
    logging.info(threading.currentThread().getName() + str(' is exiting...'))
    return


def second_function():
    logging.info(threading.currentThread().getName() + str(' is starting...'))
    time.sleep(2)
    logging.info(threading.currentThread().getName() + str(' is exiting...'))
    return


def third_function():
    logging.info(threading.currentThread().getName() + str(' is starting...'))
    time.sleep(2)
    logging.info(threading.currentThread().getName() + str(' is exiting...'))
    return

if __name__ == '__main__':
    t1 = threading.Thread(name='first_function', target=first_function)
    t2 = threading.Thread(name='second_function', target=second_function)
    t3 = threading.Thread(name='third_function', target=third_function)

    t1.start()
    t2.start()
    t3.start()

    logging.debug('Pause')
