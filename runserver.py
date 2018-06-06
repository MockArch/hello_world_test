import app
import multiprocessing
import time
import test
from multiprocessing import Process, Lock


lock = Lock()


def flask_runner():
	time.sleep(10)
	app.runserver()
    #pass

def test_runner():
    test.run_test()
    print("me test runner")


if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=flask_runner)
    d.daemon = True

    n = multiprocessing.Process(name='non-daemon', target=test_runner)
    n.daemon = False

    d.start()
    time.sleep(1)
    n.start()
    d.join()
    n.join()