# -*- coding: utf-8 -*-


from numpy import array
from numpy import pi
from numpy.random import random

from modules.glyphs import _get_glyph
from modules.utils import _export
from modules.utils import _interpolate_write_with_cursive

TWOPI = 2.0*pi


class Writer(object):
  def __init__(
      self,
      glyph_height,
      glyph_width,
      word_space,
      shift_prob,
      shift_size,
      dot_dst,
      edge
      ):
    self.i = 0

    self.glyph_height = glyph_height
    self.glyph_width = glyph_width
    self.word_space = word_space
    self.shift_prob = shift_prob
    self.shift_size = shift_size
    self.dot_dst = dot_dst

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
            gnum,
            self.glyph_height,
            self.glyph_width,
            self.shift_prob,
            self.shift_size,
            self.dot_dst
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
      cursor += self.word_space
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
            gnum,
            self.glyph_height,
            self.glyph_width,
            self.shift_prob,
            self.shift_size,
            self.dot_dst
            )
        glyphs.append(glyph)

      self._current_glyph = glyphs
      yield _export(self, glyphs, inum)
      glyphs = []

