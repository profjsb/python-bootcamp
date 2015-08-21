import numpy as np
from alloc_norm_mul import alloc_norm_mul

rng = np.random.RandomState(0)  # Sorry, Josh, -1 doesn't work

A = rng.uniform(size=((500, 100))) * 100
B = rng.uniform(size=((100, 60))) * 500

alloc_norm_mul(A, B)
