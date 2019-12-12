def main():
    print(uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))

#Gives a sentence its letters back in order. This works for all letters and is not constricted to vowels.
def uncensor(sentence, vowels):
    s = list(sentence)
    v = list(vowels)
    j = 0
    if "*" not in sentence:
        return sentence
    elif 1 > len(vowels):
        return sentence
    else:
        for i in range(len(sentence) - 1):
            if s[i] == "*":
                s[i] = v[j]
                j = j + 1
    return "".join(s)


main()
