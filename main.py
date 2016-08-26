#!/usr/bin/python3
# -*- coding: utf-8 -*-


from numpy import linspace
# from numpy import row_stack
# from numpy import ones
from numpy.random import random


BACK = [1,1,1,1]
FRONT = [0,0,0,0.0001]
RED = [1,0,0,0.01]

SIZE = 1400
ONE = 1./SIZE
EDGE = 0.1

GAMMA = 1.8


GLYPH_HEIGHT = 0.01
GLYPH_WIDTH = 0.005

GRAINS = 30
OFFSET_SIZE = 0.0015

CURSIVE_NOISE = 0.01

ROW_NUM = 20

INUM = 20000
GNUM = [2, 4]


def get_word_generator():
  def word_generator():
    while True:
      word = []
      while random()>0.15:
        r = (0.9 + random()*1.1)*GLYPH_WIDTH
        word.append(r)
      if len(word)>2:
        yield word
  return word_generator


def write(sand):
  from modules.glyphs import Glyphs
  # from modules.helpers import get_colors

  # colors = get_colors('../colors/ir.jpg')
  # nc = len(colors)

  G = Glyphs(
      GLYPH_HEIGHT,
      GLYPH_WIDTH,
      EDGE
      )

  i = 0
  for y in linspace(EDGE, 1.0-EDGE, ROW_NUM):
    print(y)
    for a, b in G.write(
        get_word_generator(),
        y,
        gnum = GNUM,
        inum = INUM,
        cursive_noise = CURSIVE_NOISE,
        offset_size = OFFSET_SIZE
        ):

      # rgba = colors[i%nc]+[0.0001]
      # sand.set_rgba(FRONT)
      sand.paint_strokes(a, b, GRAINS)
      i += 1

      # sand.set_rgba(RED)
      # xy = row_stack(G._current_glyph)
      # sand.paint_spheres(xy,ones(len(xy), 'float')*ONE*3.5,3000)


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

