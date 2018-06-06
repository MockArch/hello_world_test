#import urllib3
import json
#from bson.json_util import dumps
import requests
import unittest
import time
import os
import sys

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
	r = requests.get('http://127.0.0.1:5000/tasks')
	a = r.json()
	for ind, i in enumerate(tasks):
		for j in i.keys():
			if tasks[ind][j] == a.get('tasks')[ind][j]:
				continue
			else:
				return False
	return True


class SimplisticTest(unittest.TestCase):
	data = get_the_request()

	def test_apitest(self):
		print(self.__class__.data)
		self.assertTrue(self.__class__.data,
						msg="response not accordint to indented ")


if __name__ == '__main__':
	print("running testing ########")
	#return True
	#time.sleep(100)
	unittest.main(verbosity=2)