import numpy as np
from math import e
import time

a = time.time_ns()
f = lambda x : 1/(1+np.e**(-x))
b = time.time_ns()
print(f(10))
print(b-a)


a = time.time_ns()
f = lambda x : 1/(1+e**(-x))
b = time.time_ns()
print(f(10))
print(b-a)