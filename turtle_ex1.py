from turtle import *
shape("turtle")
n_angle = int(input("n = "))
for i in range(n_angle) :
    forward(100)
    left(360/n_angle)

mainloop()