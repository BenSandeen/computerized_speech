import numpy as np, scipy as sp, matplotlib.pyplot as plt, matplotlib, sklearn, librosa
from joblib import Parallel, delayed
from joblib.pool import has_shareable_memory
from __future__ import print_function # lets us print without newline to indicate progress
import os, os.path
import cPickle, pickle

