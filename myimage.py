#! /usr/bin/python
import cairo, math
from cairo import *

class MyImage:
    def __init__(self, width=64, height=64, surfaceName="default",
                 bgcolor=(1, 1, 1, 1)):
        self.surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        self.ctx     = cairo.Context(self.surface) 
        self.width   = width
        self.height  = height
        self.rectangle(0, 0, width, height, bgcolor)

    def write_png(self, filename):
        self.surface.mark_dirty()
        self.surface.write_to_png(filename)

    def set_color(self, color):
        if not color:
            return
        assert len(color) in (3, 4)
        if len(color) == 3:
            color = color + (1,)
        self.ctx.set_source_rgba(*color)

    def rectangle(self, x, y, width, height,
                       color=None, filled=True):
        self.set_color(color)
        self.ctx.rectangle(x, y, width, height)
        if filled:
            self.ctx.fill()

    def circle(self, x, y, radius, color=None, filled=True):
        self.set_color(color)
        self.ctx.arc(x, y, radius, 0, math.pi * 2)
        if filled:
            self.ctx.fill()
        else:
            self.ctx.stroke()

    def line(self, points, color=None, filled=False):
        self.set_color(color)
        first = points[0]
        self.ctx.move_to(*first)
        for p in points[1:]:
            self.ctx.line_to(*p)

        if filled:
            self.ctx.close_path()
            self.ctx.fill()
        else:
            self.ctx.stroke()

    def text(self, text, pos=(5, 20), color=None, font_size=20):
        assert len(pos) == 2
        self.set_color(color);
        self.ctx.move_to(*pos)
        self.ctx.select_font_face("Sans", cairo.FONT_SLANT_NORMAL,
                                  cairo.FONT_WEIGHT_NORMAL)
        self.ctx.set_font_size(font_size)
        self.ctx.show_text(text)


def main():
    im = MyImage(256, 256)
    #im.rectangle(100, 100, 56, 56, color=(1, 0, 0))
    #im.circle(120, 100, 20, color=(0, 1, 0, 0.5));

    #points = [(0, 0), (20, 30), (90, 5), (10, 30)]
    #im.line(points, color=(0, 0, 1), filled=False)
    #im.text("Hello", [1, 20])
    im.set_color((1, 0, 0))
    im.rectangle(100, 100, 56, 56)

    im.set_color((0, 1, 0, 0.5))
    im.circle(120, 100, 20);

    im.set_color((1, 0, 0))
    points = [(0, 0), (20, 30), (90, 5), (10, 30)]
    im.line(points, filled=False)

    im.set_color((0, 0, 1))
    im.text("Hello", [1, 20])

    im.write_png("test.png")


if __name__ == "__main__":
    main()



