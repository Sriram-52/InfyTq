#lex_auth_01269443477535129681

def find_duplicates(list_of_numbers):
    #start writing your code here
    res = []
    for i in set(list_of_numbers):
        if list_of_numbers.count(i) > 1:
            res.append(i)

    return res


list_of_numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
list_of_duplicates = find_duplicates(list_of_numbers)
print(list_of_duplicates)
