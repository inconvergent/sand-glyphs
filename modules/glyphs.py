# -*- coding: utf-8 -*-


from numpy import array
from numpy import column_stack
from numpy import cos
from numpy import cumsum
from numpy import pi
from numpy import sin
from numpy import row_stack
from numpy.random import randint
from numpy.random import random

from modules.helpers import random_points_in_circle
from modules.helpers import _rnd_interpolate


TWOPI = 2.0*pi


class Glyphs(object):
  def __init__(
      self,
      glyph_height,
      glyph_width,
      offset_size
      ):
    self.i = 0

    self.glyph_height = glyph_height
    self.glyph_width = glyph_width
    self.offset_size = offset_size

  def write(self, position_generator, gnum, inum):
    glyphs = []
    for x,y,new in position_generator():
      self.i += 1

      glyph = array((x, y)) + random_points_in_circle(
          gnum,
          0, 0, 0.5
          )*array((self.glyph_width, self.glyph_height))

      if not new:
        glyphs.append(glyph)
        continue

      stack = row_stack(glyphs)
      ig = _rnd_interpolate(stack, len(glyphs)*inum, ordered=True)
      glyphs = []

      a = random()*TWOPI + cumsum((1.0-2.0*random(len(ig)))*0.01)
      dd = column_stack((cos(a), sin(a)))*self.offset_size
      a = ig + dd
      b = ig + dd[::-1,:]*array((1,-1))

      yield a, b

