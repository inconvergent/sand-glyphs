# -*- coding: utf-8 -*-


from numpy import array
from numpy import column_stack
from numpy import cos
from numpy import cumsum
from numpy import pi
from numpy import zeros
from numpy import sin
from numpy import sort
from numpy import row_stack
from numpy.random import random

from modules.helpers import _rnd_interpolate


TWOPI = 2.0*pi

def _interpolate_write_with_cursive(glyphs, inum, theta, noise, offset_size):
  stack = row_stack(glyphs)
  ig = _rnd_interpolate(stack, len(glyphs)*inum, ordered=True)

  gamma = theta + cumsum((1.0-2.0*random(len(ig)))*noise)
  dd = column_stack((cos(gamma), sin(gamma)))*offset_size
  a = ig + dd
  b = ig + dd[::-1,:]*array((1,-1))
  return a, b

def _export(self, glyphs, inum):
  stack = row_stack(glyphs)
  ig = _rnd_interpolate(stack, len(glyphs)*inum, ordered=True)
  return ig

def _get_glyph(gnum, height, width):
  from modules.helpers import random_points_in_circle
  from numpy.random import randint

  if isinstance(gnum, list):
    n = randint(*gnum)
  else:
    n = gnum

  if random()<0.2:
    shift = ((-1)**randint(0,2))*1.7
  else:
    shift = 0

  if random()<0.0:
    a = sort(TWOPI*(random()+random(n)))[::-1]
    glyph = column_stack((cos(a), shift+sin(a))) \
        *array((width, height), 'float')*0.5
  else:
    glyph = random_points_in_circle(
        n, 0, shift, 0.5
        )*array((width, height), 'float')
    _spatial_sort(glyph)

  return glyph

def _spatial_sort(glyph):
  from scipy.spatial.distance import cdist
  from numpy import argsort
  from numpy import argmin

  curr = argmin(glyph[:,0])
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
      edge = 0.1
      ):
    self.i = 0

    self.glyph_height = glyph_height
    self.glyph_width = glyph_width
    self.edge = edge
    self._previous_word = None

  def write(self, word_generator, y, gnum, inum, cursive_noise, offset_size):
    glyphs = []

    theta = random()*TWOPI
    wg = word_generator()
    cursor = self.edge

    while True:
      self.i += 1

      # TODO: this could result in deadlocs for the wrong word gen.
      if not self._previous_word:
        word = next(wg)
      else:
        word = self._previous_word
        self._previous_word = None

      if (cursor+sum(word)) > (1.0-self.edge):
        self._previous_word = word
        return

      for w in word:
        cursor += w
        glyph = array((cursor, y), 'float') + _get_glyph(
            gnum, self.glyph_height, self.glyph_width
            )
        glyphs.append(glyph)

      self._current_glyph = glyphs
      yield _interpolate_write_with_cursive(
          glyphs,
          inum,
          theta,
          cursive_noise,
          offset_size
          )
      glyphs = []

  def export(self, word_generator, y, gnum, inum):
    glyphs = []

    wg = word_generator()
    cursor = self.edge

    while True:
      self.i += 1

      if not self._previous_word:
        word = next(wg)
      else:
        word = self._previous_word
        self._previous_word = None

      if (cursor+sum(word)) > (1.0-self.edge):
        self._previous_word = word
        return

      for w in word:
        cursor += w
        glyph = array((cursor, y), 'float') + _get_glyph(
            gnum, self.glyph_height, self.glyph_width
            )
        glyphs.append(glyph)

      self._current_glyph = glyphs
      yield _export(self, glyphs, inum)
      glyphs = []

