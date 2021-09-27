import numpy as np
import random
import math
import turtle as t

i=0
x=0
y=0
while i < 2000:
    x += random.randint(-30, 30)
    y += random.randint(-30, 30)
    t.goto(x,y)
    i+=1
    if (x > 200 or x < -200):
        t.goto(0,0)
        x=0
        y=0
    if (y > 200 or y < -200):
        t.goto(0,0)
        x=0
        y=0
