#lex_auth_01269446157664256093

def check_prime(number):
    #remove pass and write your logic here. if the number is prime return true, else return false
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False

    return True


def rotations(num):
    l = [num]
    no_of_digits = len(str(num))
    powTen = 10 ** (no_of_digits - 1)

    for i in range(no_of_digits - 1):
        first_digit = num // powTen
        left = (num * 10 + first_digit - (first_digit * powTen * 10))
        l.append(left)
        num = left

    return l


def get_circular_prime_count(limit):
    #remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.
    res = []
    for i in range(2, limit):
        if check_prime(i):
            l = [x for x in rotations(i) if not check_prime(x)]
            if len(l) == 0:
                res.append(i)
    return len(res)


#Provide different values for limit and test your program
print(get_circular_prime_count(100))
