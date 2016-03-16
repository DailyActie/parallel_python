"""Subclass Threading Implementation"""

import threading
import time

EXIT_FLAG = 0


class MyThread(threading.Thread):

    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print('Starting %s' % self.name)
        print_time(self.name, self.counter, 5)
        print('Exiting %s\n' % self.name)


def print_time(thread_name, delay, counter):
    while counter:
        if EXIT_FLAG:
            thread.exit()
        time.sleep(delay)
        print('%s: %s' % (thread_name, time.ctime(time.time())))
        counter -= 1

# Create new threads
thread1 = MyThread(1, 'Thread-1', 1)
thread2 = MyThread(2, 'Thread-2', 2)

# Start new threads
thread1.start()
thread2.start()

# Wait till complete
thread1.join()
thread2.join()

print('Exiting main thread!\n')
