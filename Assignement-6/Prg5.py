#lex_auth_01269442545042227276

def find_ten_substring(num_str):
    #Remove pass and write your logic here
    l = []
    for i in range(len(num_str)):
        total = 0
        a = ""
        for j in range(i, len(num_str)):
            total += int(num_str[j])
            a += num_str[j]
            if total == 10:
                l.append(a)

    return l


num_str = "2825302"
print("The number is:", num_str)
result_list = find_ten_substring(num_str)
print(result_list)
