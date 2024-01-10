n = int(input("Nhap so luong so: "))

b = []

for i in range(n):
    a = int(input())
    b.append(a)

tong = 0

for x in range(n):
    tong += b[x]

z = tong % 100

if z == 0:
    print("DEP")
elif z == 55:
    print("TRUNGBINH")
else:
    print("XAU")

