import time
from contextlib import contextmanager


class cm_timer_1:

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(cm_timer_1.__name__, time.time() - self.start_time)


@contextmanager
def cm_timer_2():

    start_time = time.time()
    yield
    print(cm_timer_2.__name__, time.time() - start_time)


if __name__ == '__main__':
    with cm_timer_1():
        for i in range(1,5):
            a=0

    with cm_timer_2():
        time.sleep(5.5)
