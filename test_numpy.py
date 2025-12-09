import numpy as np

a1D = np.array([1, 2, 3, 4])
print(a1D)

a2D = np.array([
    [1,2], 
    [3,4]
    ])
print(a2D)

a3D = np.array([[
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]])
print(a3D)

a4D = np.array([[
    [11, 22],
    [33, 44],
    [55, 66],
    [77, 88]
]])

# Addition of two list array
total = a3D + a4D
print(total)

# Max array element
max_elemnt = np.max(total)
print(max_elemnt)

# Min element
min_element = np.min(total)
print(min_element)