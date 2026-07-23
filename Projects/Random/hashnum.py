your_num = int(input("num: "))

new = [int(digit) for digit in str(your_num)]
print(new)
asci = ""


for i in new:
    if i == 1:
        print('''#
        #
        #
        #
        #''')

    elif i == 2:
        print('''###
           #
        ###
        #
        ###
        ''')