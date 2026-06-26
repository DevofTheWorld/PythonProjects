def main():
    vowels = 0
    user = input("Enter a word/phrase/sentence: ")

    for i in user:
        if i in ['a', 'e', 'i', 'o', 'u']:
            vowels += 1

    print(f"There are {vowels} vowels")

if __name__ == '__main__':
    main()
