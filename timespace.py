import numpy as np
from math import e
import time

list =[]
a = time.time_ns()
for i in range(0,10):
    for j in range(0,10):
        list.append(j)
b = time.time_ns()

print(b-a)
print(len(list))
list =[]
i = 0
j =10
a = time.time_ns()
while(i!=j):
    list.append(i)
    list.append(j)
    i+=1
    j-=1
b = time.time_ns()

print(b-a)
print(len(list))
