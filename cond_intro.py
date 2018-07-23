yob = int(input("your year of birth"))
age = 2018 - yob
print(age)

if age < 10:
    print("Baby is not allowed")
elif age < 18:
    print("Tennagers")
else:
    print("Adults")