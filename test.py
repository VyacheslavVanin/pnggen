#! /usr/bin/python
from myimage import MyImage
import random
import sys

def randomColor():
    return (random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))


def genImage(filename):
    minSize = 12
    maxSize = 300

    width = random.randint(minSize, maxSize)
    height = random.randint(minSize, maxSize)

    im = MyImage(width, height, bgcolor=randomColor())

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



