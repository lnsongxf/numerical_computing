import numpy as np
from numpy.random import rand
from cython_ftridiag import cytridiag as ct

a, b, c, x = rand(9), rand(10), rand(9), rand(10)
ct(a, b, c, x)
print x
