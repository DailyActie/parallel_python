# Notes and References

## MPI

**MPI** is an external C library for multiprocessing. It can be used with
Python via `mpi4py` package. See [README.md][1] about
installation and requirements.

Usage:
```
mpiexec -n 10 python chapter3/scatter_communication.py
```

Examples:

 - [Basic usage][2]
 - [Avoiding deadlocks][3]
 - [Point to Point communication][4] between two processes
 - [Broadcast communication][5] between one and many processes
   (send same data to multiple processes)
 - [Scatter communication][6] between
   one and many processes (send different data to multiple processes)
 - [Gather communication][7] between many
   and one (send data from many processes to one)
 - [Alltoall collective communication][8] between all processes
 - [Reduce communication][9] between many
   and one (plus reduce on the result)
 - [Communication optimisation][10] and virtual topology

## Asynchronous Programming

 - [Concurrent Futures Pooling][11] - easy way to obtain pool of threads or
   processes
 - [Asyncio basics][12] - asynchronous programming with asyncio
 - [Asyncio coroutines][13] - coroutines using in asyncio

  [1]: README.md#requirements
  [2]: chapter3/mpi4py_basic_usage.py
  [3]: chapter3/mpi4py_avoiding_deadlock.py
  [4]: chapter3/mpi4py_communication_point_to_point.py
  [5]: chapter3/mpi4py_communication_broadcast.py
  [6]: chapter3/mpi4py_communication_scatter.py
  [7]: chapter3/mpi4py_communication_gather.py
  [8]: chapter3/mpi4py_communication_alltoall.py
  [9]: chapter3/mpi4py_communication_reduce.py
  [10]: chapter3/mpi4py_communication_optimisation.py
  [11]: chapter4/concurrent_futures_pooling.py
  [12]: chapter4/asyncio_basics.py
  [13]: chapter4/asyncio_coroutine.py
