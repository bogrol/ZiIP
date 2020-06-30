import turtle
import math
pieciopak = turtle.Turtle()
kreska = int(input("Wprowadź wartość pomiędzy 1 a 100:"))
pieciopak.right(90)
x = 0
for i in range(1,kreska+1):
  if(i%5 == 0):
    pieciopak.right(135)
    pieciopak.forward(30*math.sqrt(2))
    pieciopak.right(225)
  else: 
    pieciopak.penup()
    pieciopak.goto(x*10,0)
    pieciopak.pendown()
    pieciopak.forward(30)
  x = x + 1