# -*- coding: utf-8 -*-


from numpy import array
from numpy import column_stack
from numpy import cos
from numpy import cumsum
from numpy import pi
from numpy import sin
from numpy import row_stack
from numpy import sort
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

    theta = random()*TWOPI
    for i,(x,y,new) in enumerate(position_generator()):
      self.i += 1

      angle = sort((random()*0 + random(gnum))*TWOPI)[::-1]
      glyph = array((x, y)) + column_stack((cos(angle), sin(angle))) \
          * array((self.glyph_width, self.glyph_height))
      #
      # glyph = array((x, y)) + random_points_in_circle(
      #     gnum,
      #     0, 0, 0.5
      #     )*array((self.glyph_width, self.glyph_height))

      if not new:
        glyphs.append(glyph)
        continue

      stack = row_stack(glyphs)
      ig = _rnd_interpolate(stack, len(glyphs)*inum, ordered=True)
      glyphs = []

      gamma = theta + cumsum((1.0-2.0*random(len(ig)))*0.03)
      dd = column_stack((cos(gamma), sin(gamma)))*self.offset_size
      a = ig + dd
      b = ig + dd[::-1,:]*array((1,-1))

      yield a, b

