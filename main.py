#!/usr/bin/python3
# -*- coding: utf-8 -*-


from numpy import linspace
from numpy.random import random


BACK = [1,1,1,1]
FRONT = [0,0,0,0.0001]

SIZE = 1500
ONE = 1./SIZE
EDGE = 0.1

GAMMA = 1.6

GRAINS = 40

GLYPH_WIDTH = 0.009
GLYPH_HEIGHT = 2.1*GLYPH_WIDTH

OFFSET_SIZE = 0.0025

ROW_NUM = 20
GLYPH_NUM = 0


def get_position_generator():
  def position_generator():
    for i, y in enumerate(linspace(EDGE, 1.0-EDGE, ROW_NUM)):

      x = EDGE
      start = True
      while x<1.0-EDGE:
        r = (0.3 + random()*0.7)*GLYPH_WIDTH*0.7
        if not start and random()<0.2:
          r += GLYPH_WIDTH*2
        x += r
        start = False
        yield x,y

  return position_generator


def write(sand):
  from modules.glyphs import Glyphs

  G = Glyphs(
      get_position_generator(),
      GLYPH_HEIGHT,
      GLYPH_WIDTH,
      OFFSET_SIZE
      )

  i = 0
  for a, b in G.write(gnum=[4,5], inum=10000):
    sand.paint_strokes(a, b, GRAINS)
    i += 1
    if not i%100:
      print(i)


def main():
  from sand import Sand
  from fn import Fn

  sand = Sand(SIZE)
  sand.set_bg(BACK)
  sand.set_rgba(FRONT)
  fn = Fn(prefix='./res/', postfix='.png')

  write(sand)
  # sand.set_bg(bw)
  name = fn.name()
  sand.write_to_png(name, GAMMA)


if __name__ == '__main__':
  main()

