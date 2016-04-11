import multiprocessing
import time


def foo():
    print('Starting function')
    time.sleep(0.1)
    print('Finished function')

if __name__ == '__main__':
    process = multiprocessing.Process(target=foo)
    print('Process before execution:', process, process.is_alive())
    process.start()
    print('Process running:', process, process.is_alive())
    process.terminate()
    print('Process terminated:', process, process.is_alive())
    process.join()
    print('Process joined:', process, process.is_alive())
    print('Process exit code:', process.exitcode)
