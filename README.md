[![Requirements Status](https://requires.io/github/lancelote/parallel_python/requirements.svg?branch=master)](https://requires.io/github/lancelote/parallel_python/requirements/?branch=master)

# parallel_python

Code for [Python Parallel Programming Cookbook][1] by Giancarlo Zaccone

  [1]: http://www.amazon.com/Parallel-Programming-Cookbook-Giancarlo-Zaccone/dp/1785289586

## Progress

 - [x] Chapter 1: Getting Started with Parallel Computing and Python
 - [x] Chapter 2: Thread-based Parallelism
 - [ ] Chapter 3: Process-base Parallelism
 - [ ] Chapter 4: Asynchronous Programming
 - [ ] Chapter 5: Distributed Python
 - [ ] Chapter 6: GPU programming with Python

## Requirements

 - `mpi4py` package requires `apt-get install libcr-dev mpich2`

## MPI

Exaple usage:
```bash
mpiexec -n 9 python point_to_point_communication.py
```
