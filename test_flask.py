#import urllib3
import json
#from bson.json_util import dumps
#import pytest
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
        "done": False,
        "id": 2,
        "title": "Learn Python"
    }
]


def get_the_request(count):
    #http = urllib3.PoolManager()
    #r = http.request('GET', 'http://127.0.0.1:5000/tasks')
    r  = 0
    try:
        r = requests.get('http://127.0.0.1:5000/tasks')
    except ConnectionError:
    	if count > 10:
    		count += 1
        	get_the_request(count)
        else:
        	raise RequestException()	


    a = r.json()
    print(a)
    for ind, i in enumerate(tasks):
        for j in i.keys():
            if tasks[ind][j] == a.get('tasks')[ind][j]:
                continue
            else:
                return False
    return True


class SimpleFlaskTest(unittest.TestCase):
    data = get_the_request(0)
    def test_flask(self):
    	self.assertTrue(self.__class__.data, msg="the api json response it not fine")


if __name__ == '__main__':
    print("running testing ########")
    time.sleep(100)
    unittest.main(verbosity=2)

