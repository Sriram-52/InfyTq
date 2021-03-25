#lex_auth_0127382283825971201450

def max_frequency_word_counter(data):
    word = ""
    frequency = 0
    data = data.lower()
    #start writing your code here
    #Populate the variables: word and frequenc
    unique_words = dict.fromkeys(set(data.split()), 0)

    for word in set(data.split()):
        unique_words[word] += data.split().count(word)

    max_value = max(unique_words.values())
    req_word = max([k for k, v in unique_words.items()
                   if v == max_value], key=len)

    print(req_word, unique_words[req_word])

    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work
    #print(word,frequency)


#Provide different values for data and test your program.
data = "Listen to the big clock Tick tock tick"
max_frequency_word_counter(data)
