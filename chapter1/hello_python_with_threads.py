# coding=utf-8

from threading import Thread
from time import sleep


class CookBook(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.message = 'Hello Parallel Python Cookbook!\n'

    def print_message(self):
        print(self.message)

    def run(self):
        print('Thread Starting...\n')

        x = 0
        while x < 10:
            sleep(2)
            self.print_message()
            x += 1

        print('Thread Ended\n')

# Start the main process
print('Process Started\n')

hello_python = CookBook()
hello_python.start()

print('Process Ended\n')
