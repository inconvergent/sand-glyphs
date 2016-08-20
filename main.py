#!/usr/bin/python3
# -*- coding: utf-8 -*-


from numpy import linspace
from numpy import pi
from numpy import column_stack
from numpy import cos
from numpy import sin
from numpy import array
from numpy.random import random

TWOPI = 2.0*pi

BACK = [1,1,1,1]
FRONT = [0,0,0,0.001]

SIZE = 1500
ONE = 1./SIZE
EDGE = 0.1

GRAINS = 25

GAMMA = 1.6


def make_creatures(sand):
  from modules.glyphs import Glyphs

  line_grid = linspace(EDGE, 1.0-EDGE, 40)
  row_grid = linspace(EDGE, 1.0-EDGE, 20)

  glyph_size = 0.012
  offset_size = 0.0008

  G = Glyphs(line_grid, glyph_size)

  # lines = []
  for y in row_grid:
    print(y)
    line = G.write_line(y)
    # lines.append(line)
    # sand.paint_dots(line)

    a = random(size=(len(line),1))*TWOPI
    dd = column_stack((cos(a), sin(a)))*offset_size
    l1 = line + dd
    l2 = line + dd[::-1,:]*array((1,-1))
    sand.paint_strokes(l1, l2, GRAINS)


  # last = lines.pop(0)
  # for i, line in enumerate(lines):
  #   print(i)
  #   sand.paint_strokes(last, line, GRAINS)
  #   last = line

def main():
  from sand import Sand
  from fn import Fn

  sand = Sand(SIZE)
  sand.set_bg(BACK)
  sand.set_rgba(FRONT)
  fn = Fn(prefix='./res/', postfix='.png')

  make_creatures(sand)
  # sand.set_bg(bw)
  name = fn.name()
  sand.write_to_png(name, GAMMA)


if __name__ == '__main__':
  main()

