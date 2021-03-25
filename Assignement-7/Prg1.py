#lex_auth_0127382206342184961397

def check_anagram(data1, data2):
    data1 = data1.lower()
    data2 = data2.lower()
    if set(data1) != set(data2) or len(data1) != len(data2):
        return False
    for i in range(len(data1)):
        if data1[i] == data2[i]:
            return False
    return True
    #start writing your code here


print(check_anagram("eat", "tea"))
