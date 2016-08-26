# -*- coding: utf-8 -*-

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

