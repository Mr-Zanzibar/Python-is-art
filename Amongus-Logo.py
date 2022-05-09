from turtle import *

fillcolor('red')

begin_fill()
pensize(10) # wow
right(90)
forward(50)
for n in [
    (30,200), (90,200), (30,50)
]:
    circle(n[0], 180)
    forward(n[1])
right(90)
forward(60)
end_fill()

penup()
goto(0, 100)
pendown()

fillcolor('white')
begin_fill()
for i in range(2):
  forward(50)
  circle(40, 180)
  end_fill()

penup()
goto(-122, 150)
pendown()
left(180)
fillcolor('red')
begin_fill()
for i in [20, 150]:
    forward(i)
    cirlce(10 , 90)
forward(20)
end_fill()
done()
