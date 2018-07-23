a = int(input("Nhap a"))
b = int(input("Nhap b"))
c = int(input("Nhap C"))

delta = b **2 - 4 * a * c
delta_sqrt = delta ** 0.5
x1 = (-b + delta_sqrt) / 2 * a
x2 = (-b - delta_sqrt) / 2 * a
x3 = (-b )/ 2 *a

if delta < 0 :
    print("pt vo nghiem")
elif delta == 0 :
    print("x1 = x2 = ",x3 )
else :
    print("x1 = ", x1)
    print("x2 = ", x2)


