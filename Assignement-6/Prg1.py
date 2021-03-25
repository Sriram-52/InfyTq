#lex_auth_01269442114344550475

def is_palindrome(word):
    #Remove pass and write your logic here
    word = word.lower()
    if len(word) < 2: return True
    if word[0] != word[-1]: return False
    return is_palindrome(word[1:-1])

#Provide different values for word and test your program
result=is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
