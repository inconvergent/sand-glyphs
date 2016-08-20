#!/usr/bin/python3
# -*- coding: utf-8 -*-


from numpy import linspace
from numpy import sort
from numpy.random import random


BACK = [1,1,1,1]
FRONT = [0,0,0,0.001]

SIZE = 1500
ONE = 1./SIZE
EDGE = 0.1

GRAINS = 25

GAMMA = 1.6


def make_creatures(sand):
  from modules.glyphs import Glyphs

  glyph_size = 0.012
  offset_size = 0.0008
  row_num = 20
  line_num = 30

  # line_grid = linspace(EDGE, 1.0-EDGE, 40)
  row_grid = linspace(EDGE, 1.0-EDGE, row_num)


  G = Glyphs(glyph_size)

  for y in row_grid:
    print(y)
    line_grid = sort(EDGE + random(line_num)*(1.0-2.0*EDGE))
    a, b = G.write_line(
        line_grid,
        y,
        offset_size,
        gnum=[4,6],
        inum=200000
        )

    sand.paint_strokes(a, b, GRAINS)


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

