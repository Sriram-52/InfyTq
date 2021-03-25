#lex_auth_01269446533799116898
from functools import reduce


def find_factors(num):
    res = [0]
    for i in range(1, num // 2 + 1):
        if num % i == 0 and i != num:
            res.append(i)
    return res


def check_perfect_number(number):
    total = reduce(lambda x, y: x + y, find_factors(number))
    if total == number:
        return True
    return False
    #start writing your code here


def check_perfectno_from_list(no_list):
    l = [x for x in no_list if check_perfect_number(x)]
    if l == [0]:
        return []
    return l
    #start writing your code here


perfectno_list = check_perfectno_from_list([18, 6, 4, 2, 1, 28])
print(perfectno_list)
