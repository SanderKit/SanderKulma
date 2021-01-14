#Sander Kulma
#13.01.2021
#IT20


import turtle
import random

aken = turtle.Screen()
aken.setup(500,500)
aken.title("Turtle töö - Sander")

#Harjutus 14
t = turtle.Turtle()
t.speed(0)
for i in range(100):
    t.fd(100)
    t.lt(110)

#Harjutus 4
tt = turtle.Turtle()
tt.speed(0)
pikkus = 100
nurk = 15
for o in range(5):
    tt.color("white")
    tt.fd(pikkus/2)
    tt.color("black")
    tt.lt(nurk)
    tt.fd(pikkus/2)
    for k in range(3):
        tt.lt(90)
        tt.fd(pikkus)
        
    
    tt.lt(90)
    tt.fd(pikkus/2)
    tt.color("white")
    tt.lt(90)
    tt.fd(pikkus/2)
    tt.rt(180)
    

#Harjutus 3
k = turtle.Turtle()
for i in range(4):
    k.fd(100)
    k.lt(90)
    
k.penup()
k.fd(50)
k.lt(90)
k.fd(50)
k.pendown()

for i in range(4):
    k.fd(100)
    k.rt(90)
