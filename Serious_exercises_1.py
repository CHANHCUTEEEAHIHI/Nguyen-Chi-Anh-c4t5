height = int(input("Xin mời nhập chiều cao theo cm của bạn :>"))
weight = int(input("Xin mời nhập cân nặng theo kg của bạn :>"))

BMI = weight / ((height / 100) * (height / 100))

print("Vậy chỉ số BMI của bạn là :" , BMI)

if BMI < 16 :
    print("bạn gầy vl :>")
elif 16 <= BMI < 18.5 :
    print("Bạn hơi gầy đấy :>")
elif 18.5 <= BMI < 25 :
    print("Chúc mừng bạn có body đẹp đó :>")
elif 25 <= BMI < 30 :
    print("Bạn có vẻ hơi béo rồi đó :>")
else :
    print("Bạn péo vl :<")
