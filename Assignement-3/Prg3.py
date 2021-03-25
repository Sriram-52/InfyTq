#lex_auth_01269441913243238467

def create_largest_number(number_list):
    number_list.sort(reverse=True)
    num = ""
    for i in number_list:
        num += str(i)
    return int(num)
    #remove pass and write your logic here


number_list = [23, 45, 67]
largest_number = create_largest_number(number_list)
print(largest_number)
