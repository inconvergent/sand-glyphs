#!/usr/bin/python3

from numpy.random import random
from numpy.random import randint

from numpy import array
from numpy import column_stack
from numpy import row_stack
from numpy import cos
from numpy import sin
from numpy import sort
from numpy import pi

from modules.utils import random_points_in_circle
from modules.utils import _spatial_sort

TWOPI = 2.0*pi


# def _get_glyph(gnum, height, width, shift_prob, shift_size):
#   if isinstance(gnum, list):
#     n = randint(*gnum)
#   else:
#     n = gnum
#
#   if random()<shift_prob:
#     shift = ((-1)**randint(0,2))*shift_size
#   else:
#     shift = 0
#
#   if random()<0.0:
#     a = sort(TWOPI*(random()+random(n)))[::-1]
#     glyph = column_stack((cos(a), shift+sin(a))) \
#         *array((width, height), 'float')*0.5
#   else:
#     glyph = random_points_in_circle(
#         n, 0, shift, 0.5
#         )*array((width, height), 'float')
#     _spatial_sort(glyph)
#
#   return glyph

def _get_glyph(gnum, height, width, shift_prob, shift_size):
  if isinstance(gnum, list):
    n = randint(*gnum)
  else:
    n = gnum

  glyph = random_points_in_circle(
      n, 0, 0, 0.5
      )*array((width, height), 'float')
  _spatial_sort(glyph)

  if random()<shift_prob:
    shift = ((-1)**randint(0,2))*shift_size*height
    glyph[:,1] += shift
  if random()<0.5:
    ii = randint(0,n-1,size=(1))
    xy = glyph[ii,:]
    glyph = row_stack((glyph, xy))


  return glyph
