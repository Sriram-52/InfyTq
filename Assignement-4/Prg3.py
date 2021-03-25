#lex_auth_01269444890062848087

def find_correct(word_dict):
    correct = 0
    almost_correct = 0
    wrong = 0
    for key, value in word_dict.items():
        if key == value:
            correct += 1
        elif len(key) != len(value):
            wrong += 1
        else:
            temp = 0
            for ch in range(len(value)):
                if key[ch] != value[ch]:
                    temp += 1
            if temp > 2:
                wrong += 1
            else:
                almost_correct += 1
    return [correct, almost_correct, wrong]
    #start writing your code here


word_dict = {"THEIR": "THEIR", "BUSINESS": "BISINESS",
             "WINDOWS": "WINDMILL", "WERE": "WEAR", "SAMPLE": "SAMPLE"}
print(find_correct(word_dict))
