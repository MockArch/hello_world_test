#import urllib3
import json
#from bson.json_util import dumps
import pytest
import requests
import unittest
import time
import os
import sys
from requests.exceptions import *

tasks = [
  {
	"description": "Milk, Cheese, Pizza, Fruit, Tylenol",
	"done": False,
	"id": 1,
	"title": "Buy groceries"
  },
  {
	"description": "Need to find a good Python tutorial on the web",
	"done": True,
	"id": 2,
	"title": "Learn Python"
  }
]


def get_the_request():
	#http = urllib3.PoolManager()
	#r = http.request('GET', 'http://127.0.0.1:5000/tasks')
	try:
		r = requests.get('http://127.0.0.1:5000/tasks')
	except ConnectionError:
		time.sleep(10)
		get_the_request()

	a = r.json()
	print(a)
	for ind, i in enumerate(tasks):
		for j in i.keys():
			if tasks[ind][j] == a.get('tasks')[ind][j]:
				continue
			else:
				return False
	return True



def test_apitest():
	data = get_the_request()
	assert data == True , "The api response is not equal to assigned"


if __name__ == '__main__':
	print("running testing ########")
	#return True
	#time.sleep(100)
	unittest.main(verbosity=2)