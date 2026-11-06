import numpy as np

arr0D = np.array(42)
print(arr0D)
print( type(arr0D) )
print(arr0D.ndim)

arr1D = np.array([1,2,3])
print(arr1D)
print( type(arr1D) )
print(arr1D.ndim)

b = [[1,2,3],[4,5,6]]
print(b[0][0])

arr2D = np.array([[1,2,3],[4,5,6]])
print(arr2D)
print(type(arr2D))
print(arr2D.ndim)
print(arr2D[0,0])