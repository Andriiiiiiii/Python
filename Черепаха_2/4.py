import numpy as np
import turtle as t
import math 
x=0
y=0.01
ay =-9.81
dt =0.1
Vx = 5
Vy = 70
while x<500:
    x += Vx*dt
    y += Vy*dt + ay*dt**2/2
    Vy += ay*dt
    t.goto(x,y)
    if (y <= 0):
        Vy = math.fabs(Vy)
        Vy /= 1.3
    print(y)
