print('''1. Tinh cong
2. Tinh tru
3. Ting nhan
4. Ting chia''')

while True:
    answer = int(input("Chon mot kieu tinh: "))
    if answer == 1 or answer == 2 or answer == 3 or answer == 4:
        number_1 = int(input("So 1: "))
        number_2 = int(input("So 2: "))
        if answer == 1:
            print(f"{number_1} + {number_2} = {number_1 + number_2}")
            break
        elif answer == 2:
            print(f"{number_1} - {number_2} = {number_1 - number_2}")
            break
        elif answer == 3:
            print(f"{number_1} * {number_2} = {number_1 * number_2}")
            break
        elif answer == 4:
            print(f"{number_1} : {number_2} = {number_1 / number_2}")
            break
    else:
        print("Lua chon minh khong hop le")

