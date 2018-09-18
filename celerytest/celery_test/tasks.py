#!/usr/bin/env python
# coding=utf-8

from celery import Celery

app = Celery('task', broker='redis://127.0.0.1:6379/5')

@app.task
def add(x, y):
    return x + y

