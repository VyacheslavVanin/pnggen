#! /usr/bin/python
import cairo, math
from cairo import *

class MyImage:
    def __init__(self, width=64, height=64, surfaceName="default",
                 bgcolor=(1,1,1)):
        svgName = surfaceName + ".svg"
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        self.ctx     = cairo.Context(self.surface) 
        self.width   = width
        self.height  = height
        self.draw_rectangle(0, 0, width, height, color=bgcolor)

    def write_png(self, filename):
        self.surface.write_to_png(filename)

    def set_color(self, color):
        self.ctx.set_source_rgb(color[0], color[1], color[2])

    def draw_rectangle(self, x, y, width, height, color=(0,0,0), filled=True):
        self.set_color(color)
        self.ctx.rectangle(x,y,width,height)
        if filled:
            self.ctx.fill()

    def draw_circle(self, x, y, radius, color=(0,0,0), filled=True):
        self.set_color(color)
        self.ctx.arc(x, y, radius, 0, math.pi*2)
        if filled:
            self.ctx.fill()
        else:
            self.ctx.stroke()

    def draw_line(self, points, color=(0,0,0), filled=False):
        self.set_color(color)
        self.ctx.move_to(points[0][0], points[0][1])
        for p in points[1:]:
            self.ctx.line_to(p[0], p[1])
        if filled:
            self.ctx.close_path()
            self.ctx.fill()
        else:
            self.ctx.stroke()


def main():
    im = MyImage(256, 256, bgcolor=(0,0,0))
    im.draw_rectangle(100, 100, 56, 56, color=(1,0,0))
    im.draw_circle(120, 120, 20, color=(0,1,0), filled=False);

    points = [(0,0), (20,30), (90, 5), (10, 30)]
    im.draw_line(points, color=(0,0,1), filled=True)

    im.write_png("test.png")


if __name__ == "__main__":
    main()



