#lex_auth_012693816331657216161
from itertools import groupby


def encode(message):
    s = ""
    for key, group in groupby(message):
        s += str(len(list(group))) + key
    #Remove pass and write your logic here
    return s


#Provide different values for message and test your program
encoded_message = encode("ABBBBCCCCCCCCAB")
print(encoded_message)
