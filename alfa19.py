import numpy as np

arr = np.array([1.1,2.1,3.1])
arr1 = np.array([1,0,3])
newarr1 = arr1.astype(bool)

newarr = arr.astype(int)
print(arr.dtype)
print(newarr)
print(newarr.dtype)
print(newarr1)
print(newarr1.dtype)

