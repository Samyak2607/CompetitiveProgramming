import numpy as np
import time

a = np.random.rand(1000000000)
b = np.random.rand(1000000000)

start = time.time()

c = np.dot(a,b)
end = time.time()

print('Vectorization time:',end-start)

c=0
start = time.time()
for i in range(len(a)):
    c+=a[i]*b[i]
end = time.time()

print('For loop time:', end-start)
