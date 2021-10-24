import random


class Unique:

    def __init__(self, items, **kwargs):
        self.used_elements = set()
        self.data = list(items)
        self.index = 0
        if 'ignore_case' in kwargs.keys() and kwargs['ignore_case'] == True:
            self.ignore_case = True
        else:
            self.ignore_case = False

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            current = self.data[self.index]
            self.index += 1
            if ((self.ignore_case or not isinstance(current, str)) and current not in self.used_elements):
                self.used_elements.add(current)
                return current
            elif (not self.ignore_case and isinstance(current, str)
                    and current.upper() not in self.used_elements
                    and current.lower() not in self.used_elements):
                self.used_elements.add(current.upper())
                self.used_elements.add(current.lower())
                return current

    def __iter__(self):
        return self


def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield random.randint(begin, end)


if __name__ == '__main__':
    data_int = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    data_rand = gen_random(10, 3, 10) 
    data_str = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print('Отбор уникальных чисел: ', str(list(Unique(data_int)))[1:-1])
    print('Отбор уникальных случайных чисел: ', str(list(Unique(data_rand)))[1:-1])
    print('Отбор уникальных строк без игнорирования регистра по умолчанию: ', str(list(Unique(data_str)))[1:-1])
    print('Отбор уникальных строк (регистр учитывается): ', str(list(Unique(data_str, ignore_case=True)))[1:-1])
    print('Отбор уникальных строк (регистр НЕ учитывается): ', str(list(Unique(data_str, ignore_case=False)))[1:-1])
