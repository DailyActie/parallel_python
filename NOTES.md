# Notes and References

## MPI

**MPI** is an external C library for multiprocessing. It can be used with
Python via `mpi4py` package. See [README.md](README.md#requirements) about
installation and requirements.

Usage:
```
mpiexec -n 10 python chapter3/scatter_communication.py
```

Examples:

 - [Basic usage](chapter3/mpi4py_basic_usage.py)
 - [Avoiding deadlocks](chapter3/mpi4py_avoiding_deadlock.py)
 - [Point to Point communication](chapter3/mpi4py_communication_point_to_point.py)
   between two processes
 - [Broadcast communication](chapter3/mpi4py_communication_broacast.py) between
   one and many processes (send same data to multiple processes)
 - [Scatter communication](chapter3/mpi4py_communication_scatter.py) between
   one and many processes (send different data to multiple processes)
