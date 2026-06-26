def main(num):
    if num == 0:
        return 0

    return (num % 10) + main(num // 10)

print(main(2345))
