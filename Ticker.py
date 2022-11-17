import time
from threading import Thread


# Run a function periodically
# in background


def ticker():

    def task():
        print('123')    # function
        time.sleep(1)   # interval
        ticker()

    thread = Thread(target = task, daemon = True)

    thread.start()

    time.sleep(0.5)


# Testing

ticker()
time.sleep(10)
