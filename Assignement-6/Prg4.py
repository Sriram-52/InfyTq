#lex_auth_01269442760027340879

def find_divisors(num):
    l = []
    for i in range(1, num + 1):
        if num % i == 0:
            l.append(i)

    return l


def find_smallest_number(num):
    req_num = 0
    while len(find_divisors(req_num)) != num:
        req_num += 1
    return req_num
    #start writing your code here


num = 16
print("The number of divisors :", num)
result = find_smallest_number(num)
print("The smallest number having", num, " divisors:", result)
