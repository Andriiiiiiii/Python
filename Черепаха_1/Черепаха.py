import numpy as np

def ex3():
    t.right(45)
    t.circle(100, 360, 4)
def ex4():
    t.circle(100)
def ex5():
    #t.right(45)
    i=10
    while i<100:
        t.pendown()
        t.circle(i*np.sqrt(2),360,4)
        t.penup()
        t.right(45)
        t.forward(10)
        t.right(90)
        t.forward(10)
        t.left(135)
        i=i+10
def ex6():
    n=12
    i=0
    while i<n:
        t.forward(100)
        t.stamp()
        t.backward(100)
        t.right(360/n)
        i = i+1
def ex7():
    x=0
    while x<3:
        t.forward(x)
        t.left(1)
        x=x+0.005
def ex8():
    i=10
    while i<100:
        t.forward(i)
        t.left(90)
        i+=5
def ex9():
    i=30
    x=3
    y=0
    while x<11:
        t.penup()
        t.goto(0,y)
        t.pendown()
        t.circle(i, 360, x)
        i=i+20
        x=x+1
        y=y-20
def ex10():
    n=1
    while n<7:
        t.circle(50)
        t.left(60)
        n=n+1
def ex11():
    i=0
    while i<50:
        t.circle(100+i)
        t.left(180)
        t.circle(100+i)
        i=i+10
def ex12():
    t.right(90)
    i=0
    while i<5:
        t.circle(50,180)
        t.circle(10,180)
        i=i+1
def ex13():
    t.color('red', 'yellow')
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    t.penup()
    t.goto(-40,120)
    t.pendown()
    t.color('red', 'blue')
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    t.penup()
    t.goto(40,120)
    t.pendown()
    t.color('red', 'blue')
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    t.penup()
    t.color('black')
    t.goto(0,100)
    t.width(5)
    t.pendown()
    t.goto(0,70)

    t.penup()
    t.goto(-50,70)
    t.pendown()

    t.width(7)
    t.color('red')
    t.right(90)
    t.circle(50, 180)
def ex14():
    i=0
    while i<5:
        t.forward(100)
        t.right(144)
        i=i+1
def ex15():
    i=0
    while i<11:
        t.forward(100)
        t.right(180-180/11)
        i=i+1


while 3<5:
    x=int(input("Какое упражнение вы хотите увидеть? "))
    import turtle as t
    t.shape('turtle')
    t.clear()
    t.penup()
    t.goto(0,0)
    t.color('black')
    t.width(1)
    t.pendown()
    t.setheading(0)
    if x==3:
        ex3()
    if x==4:
        ex4()
    if x==5:
        ex5()
    if x==6:
        ex6()
    if x==7:
        ex7()
    if x==8:
        ex8()
    if x==9:
        ex9()
    if x==10:
        ex10()
    if x==11:
        ex11()
    if x==12:
        ex12()
    if x==13:
        ex13()
    if x==14:
        ex14()
    if x==15:
        ex15()
    if x==16:
        break 

    






