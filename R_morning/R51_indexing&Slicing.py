# indexing and Slicing
# 2D Array


import numpy as np
arr1 = np.arange(5,15)
arr1
# array([ 5,  6,  7,  8,  9, 10, 11, 12, 13, 14])


arr1[2]         # 7


arr1[5]     # 10


arr1[3:8]       #array([ 8,  9, 10, 11, 12])


arr1        #array([ 5,  6,  7,  8,  9, 10, 11, 12, 13, 14])


arr1[3:8:2]     #array([ 8, 10, 12])


arr1[::-1]          #array([14, 13, 12, 11, 10,  9,  8,  7,  6,  5])


# 2d
arr2 = np.arange(15).reshape(5,3)
arr2
# array([[ 0,  1,  2],
#        [ 3,  4,  5],
#        [ 6,  7,  8],
#        [ 9, 10, 11],
#        [12, 13, 14]])


arr2[0]     #array([0, 1, 2])

arr2[3]     #array([ 9, 10, 11])

arr2[0:3]       # array([[0, 1, 2],
                # [3, 4, 5],
                # [6, 7, 8]])


arr2[0:2]
# array([[0, 1, 2],
#        [3, 4, 5]])
arr2
# array([[ 0,  1,  2],
#        [ 3,  4,  5],
#        [ 6,  7,  8],
#        [ 9, 10, 11],
#        [12, 13, 14]])


arr2[0:2,0:2]
# array([[0, 1],
#        [3, 4]])


# arr2[rows,col]
# arr2[strat_rows:end_rows,start_col:end_col]
arr2[1:3,1:3]
# array([[4, 5],
#        [7, 8]])


arr2[1:3,1:]
# array([[4, 5],
#        [7, 8]])


# Indexing with Boolean value arrays
# Indexing with Boolean value arrays
# fancy masking
# boolean Masking
arr3 = np.arange(12)
arr3
#O/P:- array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])


print(10>5)
# O/P:- True


arr3 > 5
# array([False, False, False, False, False, False,  True,  True,  True,
#         True,  True,  True])


arr3 > 10
# array([False, False, False, False, False, False, False, False, False,
#        False, False,  True])


arr3%2 ==0
# array([ True, False,  True, False,  True, False,  True, False,  True,
#        False,  True, False])


arr3%3 ==0
# array([ True, False, False,  True, False, False,  True, False, False,
#         True, False, False])


arr3
# array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])


arr3%2 ==0 and arr3%3 ==0
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# Input In [44], in <cell line: 1>()
# ----> 1 arr3%2 ==0 and arr3%3 ==0
#
# ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()



(arr3 % 2 == 0) & (arr3 % 3 == 0)
# array([True, False, False, False, False, False, True, False, False,
#        False, False, False])



(arr3 % 2 == 0) | (arr3 % 3 == 0)
# array([True, False, True, True, True, False, True, False, True,
#        True, True, False])


arr3[(arr3 % 2 == 0) | (arr3 % 3 == 0)]
# array([0, 2, 3, 4, 6, 8, 9, 10])


arr4 = arr3[arr3 % 2 == 0]
arr3
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])


arr4
# array([0, 2, 4, 6, 8, 10])


arr5 = np.arange(12).reshape(3, 4)
arr5
# array([[0, 1, 2, 3],
#        [4, 5, 6, 7],
#        [8, 9, 10, 11]])


arr5[arr3 % 2 == 0]  # o/p will be 1D array
# array([0, 2, 4, 6, 8, 10])





