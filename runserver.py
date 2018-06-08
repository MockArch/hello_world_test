import app
import multiprocessing
import time
# import test
import pytest
from multiprocessing import Process, Lock
from test_flask import get_the_request, tasks
import os


lock = Lock()
FILE_NAME = '/test_flask.py'

def flask_runner():
	# time.sleep(10)
	app.runserver()
	# pass


def app_test_runner():
	est_flask()
	#data = get_the_request()
	#assert data == True , "The api response is not equal to assigned"


if __name__ == '__main__':
	d = multiprocessing.Process(name='daemon', target=flask_runner)
	dir(d)
	d.daemon = True

	n = multiprocessing.Process(name='non-daemon', target=app_test_runner)
	n.daemon = False

	d.start()
	#time.sleep(1)
	n.start()
	d.join()
	n.join()
