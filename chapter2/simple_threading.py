# coding=utf-8

"""Simple threading example"""

import threading


def function(i):
    print('Function called by thread %i\n' % i)

threads = []
for i in range(5):
    t = threading.Thread(target=function, args=(i,))
    threads.append(t)
    t.start()
    t.join()  # Wait until thread is finished
