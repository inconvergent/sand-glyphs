# -*- coding: utf-8 -*-

from modules.helpers import _rnd_interpolate
from numpy.random import randint
from numpy import row_stack
# from modules.helpers import _interpolate
from modules.helpers import random_points_in_circle


class Glyphs(object):
  def __init__(
      self,
      glyph_size
      ):
    self.i = 0

    self.glyph_size = glyph_size

  def write_line(self, line_grid, y, gnum=[5,8], inum=200000):

    glyphs = []
    for x in line_grid:
      glyph = random_points_in_circle(
          randint(*gnum),
          x, y,
          self.glyph_size
          )
      glyphs.append(glyph)

    line = _rnd_interpolate(row_stack(glyphs), inum, ordered=True)
    return line

