x = input("Mời bạn nhập các ký tự tùy ý :")
x = x.lower()
x.split()


Dict = {}

for i in x :
    Dict[i] = x.count(i)



print(Dict)

