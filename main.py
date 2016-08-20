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

GRAINS = 25

GLYPH_WIDTH = 0.009
GLYPH_HEIGHT = 2.1*GLYPH_WIDTH

OFFSET_SIZE = 0.0025

ROW_NUM = 20


def get_position_generator(y):
  def position_generator():
    x = EDGE
    c = 0
    while x<1.0-EDGE:
      r = (0.3 + random()*0.7)*GLYPH_WIDTH*0.7
      new = False

      if c>0 and random()<0.1:
        r += GLYPH_WIDTH*2
        new = True
        c = 0
      x += r
      if not new:
        c += 1
      yield x,y,new
  return position_generator


def write(sand):
  from modules.glyphs import Glyphs

  G = Glyphs(
      GLYPH_HEIGHT,
      GLYPH_WIDTH,
      OFFSET_SIZE
      )

  for y in linspace(EDGE, 1.0-EDGE, ROW_NUM):
    print(y)
    for a, b in G.write(
        get_position_generator(y),
        gnum = 4,
        inum = 10000
        ):
      sand.paint_strokes(a, b, GRAINS)


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

