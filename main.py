#!/usr/bin/python3
# -*- coding: utf-8 -*-


from numpy import linspace

BACK = [1,1,1,1]
FRONT = [0,0,0,0.0001]

SIZE = 2000
ONE = 1./SIZE
EDGE = 0.1

GAMMA = 1.6


def make_creatures(sand):
  from modules.glyphs import Glyphs

  line_grid = linspace(EDGE, 1.0-EDGE, 10)
  letter_size = 0.01

  G = Glyphs(line_grid, letter_size)

  for y in line_grid:
    print(y)
    line = G.write_line(y)
    sand.paint_dots(line)

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

