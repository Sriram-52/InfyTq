#lex_auth_01269445968039936095

def add_upto_single_digit(x):
    if x == 0:
        return 0
    if x % 9 == 0:
        return 9
    return x % 9


def validate_credit_card_number(card_number):
    #start writing your code here\
    evenIndex = []
    oddIndex = []
    card_num_rev = str(card_number)[::-1]
    for num in range(len(card_num_rev)):
        i = int(num)
        r = int(card_num_rev[i])
        if i % 2:
            evenIndex.append(r)
        else:
            oddIndex.append(r)
    evenIndex = list(map(lambda x: x * 2, evenIndex))
    evenIndex = list(map(add_upto_single_digit, evenIndex))
    if (sum(oddIndex) + sum(evenIndex)) % 10:
        return False
    return True


# 4539869650133101  #1456734512345698 # #5239512608615007
card_number = 1456734512345698
result = validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")
