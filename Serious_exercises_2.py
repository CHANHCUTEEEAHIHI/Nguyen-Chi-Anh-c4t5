n = int(input("Mời bạn nhập số n :"))

factorial = 1
for i in range(1, n + 1):
    factorial *= i

print("giai thừa của số n là :", factorial)
