#lex_auth_01269446319507046499

def remove_duplicates(value):
    s = ""
    for ch in value:
        if ch not in s:
            s += ch
    return s
    #start writing your code here


print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
