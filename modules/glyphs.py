# -*- coding: utf-8 -*-


from numpy import array
from numpy import column_stack
from numpy import cos
from numpy import cumsum
from numpy import sort
from numpy import pi
from numpy import sin
from numpy import row_stack
from numpy.random import random

from modules.helpers import _rnd_interpolate


TWOPI = 2.0*pi

def _write_with_cursive(self, glyphs, inum, theta):
  stack = row_stack(glyphs)
  ig = _rnd_interpolate(stack, len(glyphs)*inum, ordered=True)

  gamma = theta + cumsum((1.0-2.0*random(len(ig)))*0.03)
  dd = column_stack((cos(gamma), sin(gamma)))*self.offset_size
  a = ig + dd
  b = ig + dd[::-1,:]*array((1,-1))
  return a, b

def _get_glyph(gnum, height, width):
  from modules.helpers import random_points_in_circle

  if isinstance(gnum, list):
    from numpy.random import randint
    f = lambda: randint(*gnum)
  else:
    f = lambda: gnum

  a = sort(TWOPI*random(f()))[::-1]
  glyph = column_stack((cos(a), sin(a)))*array((width, height), 'float')*0.5

  # glyph = + random_points_in_circle(
  #     f(), 0, 0, 0.5
  #     )*array((width, height), 'float')
  # _spatial_sort(glyph)

  return glyph

def _spatial_sort(glyph):
  from scipy.spatial.distance import cdist
  from numpy import argsort
  curr = 0
  visited = set([curr])
  order = [curr]

  dd = cdist(glyph, glyph)

  while len(visited)<len(glyph):
    row = dd[curr,:]

    for i in argsort(row):
      if row[i]<=0.0 or i==curr or i in visited:
        continue
      order.append(i)
      visited.add(i)
      break
  glyph[:,:] = glyph[order,:]


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
    pg = position_generator()
    try:
      while True:
        self.i += 1
        x, y, new = next(pg)

        glyph = array((x, y), 'float') + _get_glyph(
            gnum, self.glyph_height, self.glyph_width
            )

        if not new:
          glyphs.append(glyph)
          continue

        yield _write_with_cursive(self, glyphs, inum, theta)
        glyphs = []

    except StopIteration:
      try:
        yield _write_with_cursive(self, glyphs, inum, theta)
      except ValueError:
        return
      except TypeError:
        return

