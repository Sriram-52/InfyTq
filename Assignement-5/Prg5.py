#lex_auth_01269438947391897654
from functools import reduce
#Global variable
list_of_marks = (12, 18, 25, 24, 2, 5, 18, 20, 20, 21)


def find_more_than_average():
    total = reduce(lambda x, y: x + y, list_of_marks)
    avg = total / len(list_of_marks)
    filtered_list = [x for x in list_of_marks if x > avg]
    return len(filtered_list) * 100 / len(list_of_marks)
    #Remove pass and write your logic here


def sort_marks():
    return sorted(list_of_marks)
    #Remove pass and write your logic here


def generate_frequency():
    req_list = list(list_of_marks)
    l = []
    for i in range(0, 26):
        l.append(req_list.count(i))
    return l
    #Remove pass and write your logic here


print(find_more_than_average())
print(generate_frequency())
print(sort_marks())
