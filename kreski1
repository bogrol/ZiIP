import turtle
import math
pieciopak = turtle.Turtle()
kreska = int(input("Wprowadź wartość pomiędzy 1 a 100: ")) #wprowadzanie wartości
pieciopak.right(90) # 90 oznacza kąt (w dół)
x = 0
y = 0
j = 0
for i in range(1,kreska+1):
  j = j + 1
  print (j)
  if (j == 25):
    y = y - 35
    x = x - 25
    j = 0
  if(i%5 == 0): #dla każdego 5 przejścia pętli rysujemy przekreślającą linię ukośnie
    pieciopak.right(135)
    pieciopak.forward(30*math.sqrt(2))
    pieciopak.right(225)
  else: #dla każdego przejścia pętli 1-4 rysujemy pionową linię
    pieciopak.penup()
    pieciopak.goto(x*10,y)
    pieciopak.pendown()
    pieciopak.forward(30)
  x = x + 1
