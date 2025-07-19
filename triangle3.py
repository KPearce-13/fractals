from turtle import *
import canvasvg
import numpy as np
import time
import sys

def main(rule,depth,angle):

    start=time.time()

    tracer(0)
    ht()
    size = 500 #change once to account for svg viewer

    screen = Screen()
    canvas = screen.getcanvas()
    screen._root.withdraw()

    def Alphabet(character,angle,size):
        if character=="F":
            return fd(size)
        if character=="+":
            return right(angle)
        if character=="-":
            return left(angle)
        if character=="0":
            return

    def iterate(character,rule):
        if character=="F":
            return rule
        else:
            return character

    def Dragon(word,rule,depth,angle,size):
        width(size/10)
        for i in range(0,len(word)):
            if depth==0:
                Alphabet(word[i],angle,size)
            else:
                Dragon(iterate(word[i],rule),rule,depth-1,angle,size/scaling)

    def scale(axiom,angle):
        x=0
        y=0
        heading = 0 #degrees
        for letter in axiom:
            if letter == "F":
                x+=np.cos(np.deg2rad(heading))
                y+=np.sin(np.deg2rad(heading))
            elif letter == "+":
                heading = (heading+angle)%360
            elif letter == "-":
                heading = (heading-angle)%360
        return np.hypot(x,y)

    scaling = scale(rule,angle)
    print(f"Scaling factor {f"= root {scaling**2:.0f} " if angle == 120 else ""}≈ {scaling:.2}")
    Dragon("F",rule,depth,angle,size)
    update()
    canvasvg.saveall("test.svg",getscreen().getcanvas())

    bye()
    print(f"Job done in {time.time()-start:.2f}s")

if __name__ == "__main__":
    if sys.argv[1] == "" or sys.argv[1][0] != "F":
        rule = "F"+"".join(c+"F" for c in sys.argv[1])
    else:
        rule = sys.argv[1]
    depth = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    angle = int(sys.argv[3]) if len(sys.argv) > 3 else 120

    main(rule,depth,angle)
