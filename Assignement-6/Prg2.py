#lex_auth_01269442114344550475

def is_palindrome(word):
    return word.lower() == word[::-1].lower()
    #Remove pass and write your logic here


#Provide different values for word and test your program
result = is_palindrome("MadAMa")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")
