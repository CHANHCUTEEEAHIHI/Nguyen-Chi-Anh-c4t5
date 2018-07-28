menu = ["T-shirt", "Sweater"]
print("Chào mừng đến cửa hàng bán quần áo của tui <3, cửa hàng của tui có :")

no = 1
for item in menu :
    text = "{0}. {1}".format(no, item)
    no += 1
    print(text)

new_item = input("Bạn muốn thêm gì nà? :> ")
menu.append(new_item)

no = 1
for item in menu :
    text = "{0}. {1}".format(no, item)
    no += 1
    print(text)

new_fav = input("Nhập thứ khác mà bạn thích :> :")
position = int(input("Vị trí mà bạn muốn thay thế? :")) -1
menu[position] = new_fav

no = 1
for item in menu:
    text = "{0}. {1}".format(no, item)
    no += 1
    print(text)

position = int(input("Chọn vị trí mà bạn muốn xóa")) -1
menu.pop(position)

no = 1
for item in menu:
    text = "{0}. {1}".format(no, item)
    print(text)
    no += 1





