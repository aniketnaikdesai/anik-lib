import numpy as np
from itertools import zip_longest

def transpose_num_list(x):
    return ((np.array(x)).transpose()).tolist()

def transpose_jagged_list(x):
    return list(map(list,zip_longest(*x,fillvalue=None)))