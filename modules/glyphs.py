# -*- coding: utf-8 -*-


from numpy import array
from numpy import column_stack
from numpy import cos
from numpy import cumsum
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
      position_generator,
      glyph_height,
      glyph_width,
      offset_size
      ):
    self.i = 0

    self.position_generator = position_generator
    self.glyph_height = glyph_height
    self.glyph_width = glyph_width
    self.offset_size = offset_size

  def write(self, gnum, inum):
    self.i += 1

    for x,y in self.position_generator():

      # glyph = random_points_in_circle(
      #     randint(*gnum),
      #     x, y,
      #     self.glyph_width
      #     )

      glyph = (1.0-2.0*random((randint(*gnum), 2))) * \
              array((self.glyph_width, self.glyph_height))*0.5

      ig = array((x, y)) + \
          _rnd_interpolate(glyph, inum, ordered=True)
      a = random()*TWOPI + cumsum((1.0-2.0*random(inum))*0.01)
      dd = column_stack((cos(a), sin(a)))*self.offset_size
      a = ig + dd
      b = ig + dd[::-1,:]*array((1,-1))
      yield a, b

