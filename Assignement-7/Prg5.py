#lex_auth_01269443664174284882
def is_palindrome(num):
    return str(num) == str(num)[::-1]


def nearest_palindrome(number):
    #start writitng your code here
    number += 1
    while not is_palindrome(number):
        number += 1

    return number


number = 12300
print(nearest_palindrome(number))
