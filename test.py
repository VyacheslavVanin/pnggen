#! /usr/bin/python
from myimage import MyImage
import random
import sys

def randomColor():
    return (random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))


def genImage(filename):
    minSize = 8
    maxSize = 16

    width = random.randint(minSize, maxSize) * 8
    height = random.randint(minSize, maxSize) * 8

    im = MyImage(width, height, bgcolor=(1,1,1,0))
    im.draw_rectangle(0,0, width-1, height, color = randomColor());

    points1 = [(0, 0), (width,height)]
    points2 = [(width, 0), (0, height)]
    im.draw_line(points1, color=randomColor())
    im.draw_line(points2, color=randomColor())

    im.write_png(filename)


def main():
    args = sys.argv
    numImages = int(args[1])
    for i in range(numImages):
        genImage("images/image{}.png".format(i))


if __name__ == "__main__":
    main()



