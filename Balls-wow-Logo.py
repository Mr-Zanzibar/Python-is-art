from turtle import *
bgcolor('black')
color('green')
speed(100)
hideturtle()
n = 1
p = True
while True:
    circle(n)
    if p:
      n= n - 1
    else:
      n = n + 1
      left(1)
    if n == 0 or n == 60:
        p = not p
        forward(50) # the position is shit 
