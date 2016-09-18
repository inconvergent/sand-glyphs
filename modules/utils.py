# -*- coding: utf-8 -*-

from scipy.interpolate import splprep
from scipy.interpolate import splev

from numpy.random import random

from numpy import array
from numpy import column_stack
from numpy import cos
from numpy import cumsum
from numpy import linspace
from numpy import logical_not
from numpy import pi
from numpy import reshape
from numpy import row_stack
from numpy import ones
from numpy import sin
from numpy import sort
from numpy import zeros
from numpy.linalg import norm

TWOPI = 2.0*pi



def _interpolate_write_with_cursive(glyphs, inum, theta, noise, offset_size):
  stack = row_stack(glyphs)
  ig = _rnd_interpolate(stack, len(glyphs)*inum, ordered=True)
  gamma = theta + cumsum((1.0-2.0*random(len(ig)))*noise)
  dd = column_stack((cos(gamma), sin(gamma)))*offset_size
  a = ig + dd
  b = ig + dd[:,::-1]*array((1,-1))

  return a, b


def _export(self, glyphs, inum):
  stack = row_stack(glyphs)
  ig = _rnd_interpolate(stack, len(glyphs)*inum, ordered=True)
  return ig


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


def _interpolate(xy, num_points):
  tck,u = splprep([
    xy[:,0],
    xy[:,1]],
    s=0
  )
  unew = linspace(0, 1, num_points)
  out = splev(unew, tck)
  return column_stack(out)


def _rnd_interpolate(xy, num_points, ordered=False):
  tck,u = splprep([
    xy[:,0],
    xy[:,1]],
    s=0
  )
  unew = random(num_points)
  if ordered:
    unew = sort(unew)
  out = splev(unew, tck)
  return column_stack(out)


def random_points_in_circle(n,xx,yy,rr):
  """
  get n random points in a circle.
  """

  rnd = random(size=(n,3))
  t = TWOPI*rnd[:,0]
  u = rnd[:,1:].sum(axis=1)
  r = zeros(n,'float')
  mask = u>1.
  xmask = logical_not(mask)
  r[mask] = 2.-u[mask]
  r[xmask] = u[xmask]
  xyp = reshape(rr*r,(n,1))*column_stack( (cos(t),sin(t)) )
  dartsxy  = xyp + array([xx,yy])
  return dartsxy

