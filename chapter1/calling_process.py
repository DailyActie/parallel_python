# coding=utf-8

"""
Calls called_process.py

print('Goodbye!') will not be executed
"""

import os

program = 'python'
arguments = ['called_process.py']

print('Process calling...')

# Call called_process.py
os.execvp(program, (program,) + tuple(arguments))

print('Goodbye!')
