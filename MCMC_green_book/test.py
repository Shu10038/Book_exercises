import numpy as np
import pandas as pd

import sys

print (sys.path)

import pymc3 as pm

import pystan
schools_dat = {'J': 8, 'y': [28,  8, -3,  7, -1,  1, 18, 12],
               'sigma': [15, 10, 16, 11,  9, 11, 10, 18]}
