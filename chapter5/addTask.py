"""Executes a simple task"""

from celery import Celery

app = Celery('addTask', broker='amqp://rabbit@my-rabbit//')


@app.task
def add(x, y):
    return x + y
