#lex_auth_012693813706604544157

def find_max(num1, num2):
    max_num = -1

    if num1 >= num2:
        return -1

    if num1 < 10:
        num1 = 10
    if num2 > 99:
        num2 = 99
    l = [x for x in range(num1, num2 + 1) if x % 15 == 0]
    # Write your logic here
    if len(l):
        return max(l)
    return -1


#Provide different values for num1 and num2 and test your program.
max_num = find_max(10, 15)
print(max_num)
