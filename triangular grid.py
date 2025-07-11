from turtle import *
import canvasvg
import numpy as np
import time

start=time.time()

tracer(0)
ht()

screen = Screen()
canvas = screen.getcanvas()
screen._root.withdraw()

def Alphabet(character,size):
    if character=="F":
        return fd(size)
    if character=="+":
        return right(120)
    if character=="-":
        return left(120)

def iterate(character,rule):
    if character=="F":
        return rule
    else:
        return character

def Dragon(word,rule,depth,size):
    width(size/10)
    scale = np.sqrt((len(rule)+1)/2)
    for i in range(0,len(word)):
        if depth==0:
            Alphabet(word[i],size)
        else:
            Dragon(iterate(word[i],rule),rule,depth-1,size/scale)

Dragon("F","F+F-F",10,100)
update()
canvasvg.saveall("test.svg",getscreen().getcanvas())

bye()
print(f"Job done in {time.time()-start:.2f}s")
