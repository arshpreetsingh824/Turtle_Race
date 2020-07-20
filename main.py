from turtle import *
from random import randint
speed(100)
penup()
goto(-130,150)
count = 0
while count < 15:
  pendown()
  forward(10)
  penup()
  forward(10)
  count = count + 1
goto(-130,130)
count = 0
while count < 15:
  pendown()
  forward(10)
  penup()
  forward(10)
  count = count + 1
goto(-130,110)
count = 0
while count < 15:
  pendown()
  forward(10)
  penup()
  forward(10)
  count = count + 1  
goto(-130,90)
count = 0
while count < 15:
  pendown()
  forward(10)
  penup()
  forward(10)
  count = count + 1
goto(-130,70)
count = 0
while count < 15:
  pendown()
  forward(10)
  penup()
  forward(10)
  count = count + 1
goto(-130,50)
count = 0
while count < 15:
  pendown()
  forward(10)
  penup()
  forward(10)
  count = count + 1
goto(-130,20)
count = 0
while count < 15:
  pendown()
  forward(10)
  penup()
  forward(10)
  count = count + 1
goto(-130,-10)
count = 0
while count < 15:
  pendown()
  forward(10)
  penup()
  forward(10)
  count = count + 1
goto(-130,-30)
count = 0
while count < 15:
  pendown()
  forward(10)
  penup()
  forward(10)
  count = count + 1
goto(-130,-50)
count = 0
while count < 15:
  pendown()
  forward(10)
  penup()
  forward(10)
  count = count + 1
goto(-130,-70)
count = 0
while count < 15:
  pendown()
  forward(10)
  penup()
  forward(10)
  count = count + 1  
goto(-130,-90)
count = 0
while count < 15:
  pendown()
  forward(10)
  penup()
  forward(10)
  count = count + 1  
goto(-130,-110)
count = 0
while count < 15:
  pendown()
  forward(10)
  penup()
  forward(10)
  count = count + 1  
goto(-130,-130)
count = 0
while count < 15:
  pendown()
  forward(10)
  penup()
  forward(10)
  count = count + 1 
goto(-130,-150)
count = 0
while count < 15:
  pendown()
  forward(10)
  penup()
  forward(10)
  count = count + 1
speed(0) 




lam = Turtle()
lam.color('red')
lam.shape('turtle')
lam.penup()
lam.goto(-160,150)
lam.pendown()

glenza_kaur = Turtle()
glenza_kaur.color('yellow')
glenza_kaur.shape('turtle')
glenza_kaur.penup()
glenza_kaur.goto(-160,80)
glenza_kaur.pendown()
  
pops = Turtle()
pops.color('purple')
pops.shape('turtle')
pops.penup()
pops.goto(-160,10)
pops.pendown()
  
arsh = Turtle()
arsh.color('green')
arsh.shape('turtle')
arsh.penup()
arsh.goto(-160,-60)
arsh.pendown()
for turn in range(100):
  arsh.forward(randint(1,5)) 
  lam.forward(randint(1,5))
  glenza_kaur.forward(randint(1,5))
  pops.forward(randint(1,5))


