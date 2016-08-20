# -*- coding: utf-8 -*-


from numpy import array
from numpy import column_stack
from numpy import cos
from numpy import pi
from numpy import row_stack
from numpy import sin
from numpy.random import randint
from numpy.random import random

from modules.helpers import _rnd_interpolate
from modules.helpers import random_points_in_circle

TWOPI = 2.0*pi


class Glyphs(object):
  def __init__(
      self,
      glyph_size
      ):
    self.i = 0
    self.glyph_size = glyph_size

  def write_line(self, line_grid, y, offset_size, gnum, inum):
    self.i += len(line_grid)

    glyphs = []
    for x in line_grid:
      glyph = random_points_in_circle(
          randint(*gnum),
          x, y,
          self.glyph_size
          )
      glyphs.append(glyph)


    line = _rnd_interpolate(row_stack(glyphs), inum, ordered=True)
    a = random(size=(len(line),1))*TWOPI
    dd = column_stack((cos(a), sin(a)))*offset_size
    a = line + dd
    b = line + dd[::-1,:]*array((1,-1))
    return a, b

