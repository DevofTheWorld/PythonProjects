def main():
    items = []

    for i in range(5):
        list = input(f"Please list item no. {i+1}/5:  ").lower()
        items.append(list)

    for item in items:
        print(item)

    if "milk" in items:
        print("Milk is on the list")

if __name__ == '__main__':
    main()

