#!/usr/bin/python3
# -*- coding: utf-8 -*-


from numpy import linspace
from numpy.random import random

from numpy import arange
from numpy import row_stack


BACK = [1,1,1,1]
FRONT = [0,0,0,0.6]

SIZE = 1400
ONE = 1./SIZE
EDGE = 0.1

GAMMA = 1.8


GLYPH_HEIGHT = 0.01
GLYPH_WIDTH = 0.005

ROW_NUM = 20

INUM = 200
GNUM = [2, 4]


def get_position_generator(y):
  def position_generator():
    x = EDGE
    c = 0
    while x<1.0-EDGE:
      r = (0.8 + random()*1.2)*GLYPH_WIDTH
      new = False

      if c>2 and random()<0.15:
        r += GLYPH_WIDTH*2
        new = True
        c = 0

      x += r
      if not new:
        c += 1
      yield x, y, new
  return position_generator


def write(sand):
  from modules.glyphs import Glyphs

  lines = []
  vertices = []

  vnum = 0

  G = Glyphs(
      GLYPH_HEIGHT,
      GLYPH_WIDTH
      )

  i = 0
  for y in linspace(EDGE, 1.0-EDGE, ROW_NUM):
    print(y)
    for a in G.export(
        get_position_generator(y),
        gnum = GNUM,
        inum = INUM
        ):

      sand.paint_dots(a)
      i += 1

      vertices.append(a)
      lines.append(arange(len(a)).astype('int')+vnum)
      vnum += len(a)

  return row_stack(vertices), lines


def main():
  from sand import Sand
  from fn import Fn

  from iutils.ioOBJ import export_2d as export

  sand = Sand(SIZE)
  sand.set_bg(BACK)
  sand.set_rgba(FRONT)
  fn = Fn(prefix='./res/')

  vertices, lines = write(sand)
  name = fn.name()
  sand.write_to_png(name+'.png', GAMMA)

  export('glyphs', name + '.2obj', verts=vertices, lines=lines)


if __name__ == '__main__':
  main()

