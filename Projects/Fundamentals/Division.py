def main():
    firstNum = int(input("Dividend: "))
    secondNum = int(input("Divisor: "))

    try:
        quotient = firstNum / secondNum
        print(quotient)

    except Exception as e:
        print(f"Error: cannot divide {firstNum} and {secondNum}. ({e})")

main()


