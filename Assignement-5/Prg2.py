#lex_auth_0127382164803993601239
from functools import reduce
#This verification is based on string match.


def sum_of_numbers(list_of_num, filter_func=None):
    if filter_func != None:
        list_of_num = filter_func(list_of_num)
    return reduce(lambda x, y: x + y, list_of_num)


def even(data):
    return list(filter(lambda x: x % 2 == 0, data))


def odd(data):
    return list(filter(lambda x: x % 2, data))


sample_data = range(1, 11)

print(sum_of_numbers(sample_data, None))
