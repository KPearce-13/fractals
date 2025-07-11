from turtle import *
import canvasvg
import numpy as np
import time
import sys

def main(rule,depth,size):

    start=time.time()

    tracer(0)
    ht()
    size = size*500

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
        if character=="0":
            return

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

    Dragon("F",rule,depth,size)
    update()
    canvasvg.saveall("test.svg",getscreen().getcanvas())

    bye()
    print(f"Job done in {time.time()-start:.2f}s")

if __name__ == "__main__":
    rule = "F"+"".join(c+"F" for c in sys.argv[1])
    depth = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    size = int(sys.argv[3]) if len(sys.argv) > 3 else 1

    main(rule,depth,size)
