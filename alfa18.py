import numpy as np

arr = np.array([1,2,3,4], dtype='i4')
print(arr)
print(arr.dtype)
#converting Data Type on Existing Arrays
arr1 = np.array([1.1,2.1,3.1])
newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)