#lex_auth_01269444195664691284

def is_vowel(ch):
    if ch in ['a', 'e', 'i', 'o', 'u']:
        return True
    if ch in ['A', 'E', 'I', 'O', 'U']:
        return True
    return False


def encrypt_sentence(sentence):
    words = sentence.split()
    s = ""
    for i in range(len(words)):
        if (i + 1) % 2:
            words[i] = words[i][::-1]
        else:
            vowels = []
            temp = ""
            for ch in words[i]:
                if is_vowel(ch):
                    vowels.append(ch)
                else:
                    temp += ch
            temp += "".join(vowels)
            words[i] = temp
    return " ".join(words)


sentence = "the sun rises in the east"
encrypted_sentence = encrypt_sentence(sentence)
print(encrypted_sentence)
