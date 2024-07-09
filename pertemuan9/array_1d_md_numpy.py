import numpy as np

array_1d = np.array([90,70,40,30,20,10])
print(array_1d)

rata_rata = np.mean(array_1d)
print(rata_rata)
print(np.median(array_1d))
print(np.max(array_1d))
print(np.min(array_1d))
print(np.sum(array_1d > rata_rata))
print((array_1d > rata_rata))