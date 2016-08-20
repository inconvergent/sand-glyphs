#!/usr/bin/python3
# -*- coding: utf-8 -*-


from numpy import linspace
from numpy import sort
from numpy import cumsum
from numpy import ones
from numpy.random import random


BACK = [1,1,1,1]
FRONT = [0,0,0,0.001]

SIZE = 2600
ONE = 1./SIZE
EDGE = 0.1


GAMMA = 1.6


def make_creatures(sand):
  from modules.glyphs import Glyphs

  grains = 50
  glyph_size = 0.012
  offset_size = 0.001
  row_num = 20
  glyph_num = 40

  # line_grid = linspace(EDGE, 1.0-EDGE, 40)
  row_grid = linspace(EDGE, 1.0-EDGE, row_num)


  G = Glyphs()

  for y in row_grid:
    print(y)
    # glyph_sizes = glyph_size + ones(glyph_num, 'float')
    glyph_sizes = glyph_size + cumsum((1.0-2.0*random(glyph_num))*glyph_size*0.2)
    line_grid = sort(EDGE + random(glyph_num)*(1.0-2.0*EDGE))
    a, b = G.write_line(
        line_grid,
        y,
        glyph_sizes,
        offset_size,
        gnum=[4,5],
        inum=300000
        )

    sand.paint_strokes(a, b, grains)


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

