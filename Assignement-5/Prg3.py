#lex_auth_01269441810970214471

def check_double(number):
    num = str(number)
    dou = str(number * 2)

    flag = False

    if len(num) == len(dou) and num != dou:
        for ch in num:
            if ch not in dou:
                return False
        flag = True
    return flag


#Provide different values for number and test your program
print(check_double(125874))
