def cleanword(word):

    wordclean = word.lower().replace(" ", "")

    return main(list(wordclean))



def main(char):


    if len(char) <= 1:
        return True

    if char[0] == char[-1]:
        return main(char[1:-1])

    return False

print(cleanword("No lemon no melon"))





