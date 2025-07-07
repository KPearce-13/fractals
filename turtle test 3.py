from turtle import *
import canvasvg
import numpy as np
import time

start=time.time() #for timing purposes

mode('logo') #starts oriented North

tracer(0) #don't update the screen
ht() #don't show turtle
width(0.01) #you will likely need to zoom in a lot to see this at all, so you may want to increase it at first

screen = Screen()
canvas = screen.getcanvas()
screen._root.withdraw() #close the screen after completion (my best attempt at not showing it at all, but it's needed for canvasvg

def Koch(depth,size):
##    width(size/10)
    if depth==0:
        forward(size)
        return
    else:
        Koch(depth-1,size/3)
        left(60)
        Koch(depth-1,size/3)
        right(120)
        Koch(depth-1,size/3)
        left(60)
        Koch(depth-1,size/3)

##Koch(10,100)
##update()
##canvasvg.saveall("test.svg",getscreen().getcanvas())
##clearscreen()

def Alphabet(character,size):
    if character=="A":
        return fd(size)
    if character=="B":
        return fd(size)
    if character=="+":
        return right(90)
    if character=="-":
        return left(90)

P={'A': 'B', 'B': 'A', '+': '-', '-': '+'}

def iterate(character,rule):
    if character=="A":
        return rule
    if character=="B":
        return "".join(P[c] for c in reversed(rule)) #symmetry operation to obtain B for paper-folding on a square grid
    if character=="+":
        return "+"
    if character=="-":
        return "-"

def Dragon1(word,rule,depth,size):
    width(size/10)
    for i in range(0,len(word)):
        if depth==0:
            Alphabet(word[i],size)
        else:
            Dragon1(iterate(word[i],rule),rule,depth-1,size/np.sqrt(10)) # root 10 is the incorrect multiplier, but this is correct for the case Helena showed us

def Dragon2(shortrule,depth,name): #an attempt at simplifying the input
    rule = "A"+"".join(f"{c}{'BA'[i%2]}" for i,c in enumerate(shortrule))
    Dragon1("A",rule,depth,100)
    update()
    canvasvg.saveall(name,getscreen().getcanvas())
    
Dragon2("+-+-+++--",5,"test.svg") #save as an svg, which you can open in your browser

bye()
print(f"Job done in {time.time()-start:.2f}s")
