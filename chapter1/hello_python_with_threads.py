import logging
from threading import Thread
from time import sleep

logging.basicConfig(level=logging.INFO)
logger_thread = logging.getLogger('__thrd__')
logger_main = logging.getLogger(__name__)


class ParallelPython(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.message = 'Hello Parallel Python!'

    def print_message(self):
        print(self.message)

    def run(self):
        logger_thread.info('Thread Starting')

        x = 0
        while x < 10:
            sleep(2)
            self.print_message()
            x += 1

        logger_thread.info('Thread Ended')


if __name__ == '__main__':
    logger_main.info('Process Started')
    hello_python = ParallelPython()
    hello_python.start()
    logger_main.info('Process Ended')
