import time

class cm_timer_1:

    def __enter__(self):
        self.start_time = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(cm_timer_1.__name__, time.time() - self.start_time)


def print_result(func):
    start_time = time.time()
    def decorated_func(*args):  
        print(func.__name__)
        return_value = func(*args)
        if isinstance(return_value, list):
            for value in return_value:
                print(str(value))
        elif isinstance(return_value, dict):
            
            for key in return_value.keys():
                print(str(key) + ' = ' + str(return_value[key]))
            
        else:
            print(return_value)
        return return_value
    print(cm_timer_1.__name__, time.time() - start_time)
    return decorated_func




@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('______________')

    test_1() 
    test_2()
    test_3()
    test_4()
