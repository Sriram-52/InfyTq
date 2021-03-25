#lex_auth_01269444961482342489

def sms_encoding(data):
    #start writing your code here
    words = data.split()
    for i in range(len(words)):
        if len(words[i]) > 1:
            for vowel in ['a', 'e', 'i', 'o', 'u']:
                words[i] = words[i].replace(vowel, "")
            for vowel in ['A', 'E', 'I', 'O', 'U']:
                words[i] = words[i].replace(vowel, "")

    return " ".join(words)


data = "I love Python"
print(sms_encoding(data))
