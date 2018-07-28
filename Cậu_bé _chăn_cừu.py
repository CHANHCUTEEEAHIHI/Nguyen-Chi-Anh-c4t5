sheeps_sizes = [5, 7, 300, 90, 24, 50, 75]
print("Xin chào, tớ là Chí Anh và đây là kích cỡ của lũ cừu nhà tớ :D", sheeps_sizes)

highest = max(sheeps_sizes)
print("Sau 1 tháng thì chú cừu to nhất của tớ có kích cỡ :", highest, "," "hãy cùng gọt nó nào :D")

x = sheeps_sizes.index(highest)
sheeps_sizes[x] =  8
print("Sau khi gọt thì :",sheeps_sizes)

sheeps_sizes_1 =  [x + 50 for x in sheeps_sizes]
print("1 tháng đã trôi qua và lũ cừu của mình cũng béo lên :" ,sheeps_sizes_1)

highest = max(sheeps_sizes_1)
print("Sau 1 tháng nữa thì chú cừu to nhất của tớ có kích cỡ :", highest, "," "hãy cùng gọt nó nào :D")

x = sheeps_sizes_1.index(highest)
sheeps_sizes_1[x] =  8
print("Sau khi gọt thì :",sheeps_sizes_1)

sheeps_sizes_2 =  [x + 50 for x in sheeps_sizes_1]
print("1 tháng nữa đã trôi qua và lũ cừu của mình cũng béo lên :" ,sheeps_sizes_2)

highest = max(sheeps_sizes_2)
print("Sau 1 tháng nữa thì chú cừu to nhất của tớ có kích cỡ :", highest, "," "hãy cùng gọt nó nào :D")

x = sheeps_sizes_2.index(highest)
sheeps_sizes_2[x] =  8
print("Sau khi gọt thì :",sheeps_sizes_2)

sheeps_sizes_3 =  [x + 50 for x in sheeps_sizes_2]
print("1 tháng nữa đã trôi qua và lũ cừu của mình cũng béo lên :" ,sheeps_sizes_3)

Tổng = sum(sheeps_sizes_3)
print("Tổng kích cỡ đàn cừu trong tháng thú 3 của tớ là :", Tổng)

money = Tổng * 2
print("Tổng số tiền mà tớ có nếu bán lũ cừu :", money)








