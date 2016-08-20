#!/usr/bin/python3
# -*- coding: utf-8 -*-


from numpy import linspace
from numpy import sort
from numpy.random import random


BACK = [1,1,1,1]
FRONT = [0,0,0,0.0001]

SIZE = 1500
ONE = 1./SIZE
EDGE = 0.1

GAMMA = 1.6

GRAINS = 60

GLYPH_WIDTH = 0.008
GLYPH_HEIGHT = 2*GLYPH_WIDTH

OFFSET_SIZE = 0.002

ROW_NUM = 25
GLYPH_NUM = 70


def get_position_generator():
  def position_generator():
    for y in linspace(EDGE, 1.0-EDGE, ROW_NUM):
      for x in sort(EDGE + random(GLYPH_NUM)*(1.0-2.0*EDGE)):
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

