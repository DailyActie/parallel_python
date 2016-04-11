import multiprocessing


def foo(i):
    print('Called function in process: %s' % i)
    return

if __name__ == '__main__':
    process_jobs = []
    for i in range(5):
        process = multiprocessing.Process(target=foo, args=(i,))
        process_jobs.append(process)
        process.start()
        process.join()
