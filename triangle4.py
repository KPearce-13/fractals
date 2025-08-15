from turtle import *
import canvasvg
import numpy as np
import time
import sys

def main(rule,depth):

    start=time.time()

    tracer(0)
    ht()
    size = 500 #change once to account for svg viewer

    screen = Screen()
    canvas = screen.getcanvas()
    screen._root.withdraw()

    def Alphabet_0(character,size):
        if character=="F":
            return fd(size)
        if character=="+":
            return right(120)
        if character=="-":
            return left(120)
    
    def Alphabet_1(character,size):
        if character=="R":
            fd(np.sqrt(3)/3*size)
            right(60)
            fd(np.sqrt(3)/3*size)
            return
        if character=="L":
            fd(np.sqrt(3)/3*size)
            left(60)
            fd(np.sqrt(3)/3*size)
            return
        if character=="+":
            return right(60)
        if character=="-":
            return left(60)

    def iterate_0(character,rule):
        if character=="F":
            return rule
        else:
            return character

    def P_0(word,rule,depth,size):
        width(size/10)
        for i in range(0,len(word)):
            if depth==0:
                Alphabet_0(word[i],size)
            else:
                P_0(iterate_0(word[i],rule),rule,depth-1,size/scaling)

    def iterate_1(character,rule_L,rule_R):
        if character=="R":
            return rule_L
        elif character=="L":
            return rule_R
        else:
            return character

    def P_1(word,rule_L,rule_R,depth,size):
        width(size/10)
        for i in range(0,len(word)):
            if depth==0:
                Alphabet_1(word[i],size)
            else:
                P_1(iterate_1(word[i],rule_L,rule_R),rule_L,rule_R,depth-1,size/scaling)

    def scale(axiom):
        x,y = 0.0,0.0
        heading = 0 #units of 120 degrees CW from +x
        directions = [(1.0,0.0), (-0.5,-np.sqrt(3)/2), (-0.5,np.sqrt(3)/2)]
        for letter in axiom:
            if letter == "F":
                dx,dy = directions[heading]
                x+=dx
                y+=dy
            elif letter == "+":
                heading = (heading+1)%3
            elif letter == "-":
                heading = (heading-1)%3
        return np.hypot(x,y)

    def Replace(word):
        while "v" in word:
            word = word.replace("RvR","L").replace("LvL","R").replace("LvR","v").replace("RvL","v").replace("+v+","-").replace("-v-","+").replace("-v+","v").replace("+v-","v")
        return word
    
    CreateLeft = {"F":"R","+":"+","-":"v","0":"-"}
    CreateRight = {"F":"L","+":"v","-":"-","0":"+"}
    LeftBoundary = "".join(CreateLeft[i] for i in rule)
    RightBoundary = "".join(CreateRight[i] for i in rule)

    scaling = scale(rule)
    print(f"Scaling factor = root {scaling**2:.0f} ≈ {scaling:.2}")
    rule_L = Replace(LeftBoundary)
    rule_R = Replace(RightBoundary)
    print(f"Left boundary (red): P_1(R)={rule_L}")
    print(f"Right boundary (blue): P_1(L)={rule_R}")
    color("red")
    pendown()
    left(30)
    P_1("R",rule_L,rule_R,depth,size) #left boundary
    penup()
    home()
    color("blue")
    pendown()
    right(30)
    P_1("L",rule_L,rule_R,depth,size) #right boundary
    penup()
    home()
    color("black")
    pendown()
    P_0("F",rule,depth,size) #original curve on top
    update()
    canvasvg.saveall("test.svg",getcanvas())

    bye()
    print(f"Job done in {time.time()-start:.2f}s")

if __name__ == "__main__":
    if sys.argv[1] == "" or sys.argv[1][0] != "F":
        rule = "F"+"".join(c+"F" for c in sys.argv[1])
    else:
        rule = sys.argv[1]
    depth = int(sys.argv[2]) if len(sys.argv) > 2 else 1

    main(rule,depth)
