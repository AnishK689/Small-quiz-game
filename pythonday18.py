from turtle import Turtle, Screen
from random import choice, randint
t = Turtle()
# sides = 3
# angle = 360/3
colours=["navy","green","teal","tomato","red","orange","black","purple","salmon","gold"]
directions=[0,90,180,270]

# for i in range(7):
#     t.color(choice(colours))
#     for j in range(sides):
#         t.forward(100)
#         t.right(angle)
#     if sides == 6:
#         sides += 1
#     sides += 1
#     angle = 360/sides
t.shape("circle")
i=0


t.color(choice(colours))
t.pensize(5)
t.speed("fastest")
while i<=360 :

   t.color(choice(colours))
   t.circle(100)
   t.setheading(i)
   i+=20

screen = Screen()
screen.exitonclick()
#10
#sides=100
#triangle, square, pentagon, hexagon, octagon,nanogon, decagon