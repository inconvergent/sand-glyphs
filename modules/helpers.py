# -*- coding: utf-8 -*-

from scipy.interpolate import splprep
from scipy.interpolate import splev
from numpy.random import random
from numpy import linspace
from numpy import column_stack
from numpy import sort

from numpy import zeros
from numpy import reshape
from numpy import logical_not
from numpy import array
from numpy import pi as PI
from numpy import cos
from numpy import sin


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

def get_colors(f, do_shuffle=True):
  from numpy import array
  try:
    import Image
  except Exception:
    from PIL import Image

  im = Image.open(f)
  data = array(list(im.convert('RGB').getdata()),'float')/255.0

  res = []
  for rgb in data:
    res.append(list(rgb))

  if do_shuffle:
    from numpy.random import shuffle
    shuffle(res)
  return res

def random_points_in_circle(n,xx,yy,rr):
  """
  get n random points in a circle.
  """

  rnd = random(size=(n,3))
  t = 2.*PI*rnd[:,0]
  u = rnd[:,1:].sum(axis=1)
  r = zeros(n,'float')
  mask = u>1.
  xmask = logical_not(mask)
  r[mask] = 2.-u[mask]
  r[xmask] = u[xmask]
  xyp = reshape(rr*r,(n,1))*column_stack( (cos(t),sin(t)) )
  dartsxy  = xyp + array([xx,yy])
  return dartsxy

