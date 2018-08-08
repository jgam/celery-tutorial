#tasks.py
from celery import Celery

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')# tasks is the name of celery, second is broker keyword argument

@app.task
def add(x,y):
	return x+y