import multiprocessing
from time import sleep
import logging

logging.basicConfig(level=logging.INFO)


def foo(i):
    sleep(3)
    logging.info('Called function in process: %s' % i)
    return

if __name__ == '__main__':
    process_jobs = []
    for i in range(5):
        process = multiprocessing.Process(target=foo, args=(i,))
        process_jobs.append(process)
        process.start()
        process.join()
