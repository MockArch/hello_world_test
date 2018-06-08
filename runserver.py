import app
import multiprocessing
import time
# import test
import pytest
from multiprocessing import Process, Lock
import os


lock = Lock()
FILE_NAME = '/test_flask.py'
FILE_APP = '/app.py'

END_PRO = False


def flask_runner():
    p = multiprocessing.current_process()
    print(p.pid)
    currnt = os.getcwd()
    path = currnt + FILE_APP
    print(path)
    cmd = "python" + " " + path + " " + "&"
    c = os.system(cmd)
    print(c)
    print("###########################", END_PRO)
    time.sleep(5)
    os.system("pkill -9 python")
    kill_cmd = "kill -9" + " " + str(p.pid)
    os.system(kill_cmd)


def app_test_runner():
    # time.sleep(100)
    currnt = os.getcwd()
    path = currnt + FILE_NAME
    print(path)
    END_PRO = True
    cmd = 'nosetests' + " " + path
    os.system(cmd)
    # test_flask()
    # data = get_the_request()
    # assert data == True , "The api response is not equal to assigned"


if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=flask_runner)
    d.daemon = True
    print(dir(d))
    n = multiprocessing.Process(
        name='non-daemon', target=app_test_runner)
    n.daemon = False

    d.start()
    n.start()
    d.join()
    n.join()
