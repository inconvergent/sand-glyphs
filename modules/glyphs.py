#!/usr/bin/python3

from numpy.random import random
from numpy.random import randint

from numpy import array
from numpy import pi

# from modules.utils import random_points_in_circle
from modules.utils import darts
from modules.utils import _spatial_sort

TWOPI = 2.0*pi


def _get_glyph(gnum, height, width, shift_prob, shift_size, dst):

  if random()<shift_prob:
    shift = ((-1)**randint(0,2))*shift_size
  else:
    shift = 0

  while True:
    glyph = darts(
        gnum[1], 0, shift, 0.5, dst
        )*array((width, height), 'float')
    if len(glyph)>gnum[0]:
      break
  _spatial_sort(glyph)
  return glyph

