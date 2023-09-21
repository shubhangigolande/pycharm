import numpy as np

a =  [1,2,3,4,5]
arr1 = np.array(a)
arr1
# O/P:- # array([1, 2, 3, 4, 5])


# 2D Array creation
# usng list
m = [[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8]]
m
# O/P:- [[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]]


arr2 = np.array(m)
arr2            # array([[1, 2, 3, 4, 5, 6, 7, 8],[1, 2, 3, 4, 5, 6, 7, 8]])


arr2.ndim       # 2


arr2.shape      #(2, 8)


arr2.size   # 16


# using aranage() and reshape()
arr3  = np.arange(12)
print(arr3)
print(arr3.ndim)
print(arr3.shape)
print(arr3.size)
#O/P:-# [ 0  1  2  3  4  5  6  7  8  9 10 11]
# 1
# (12,)
# 12

arr3        #array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11])


# reshaping the array ()
arr3.reshape(2,6)
# array([[ 0,  1,  2,  3,  4,  5],
#        [ 6,  7,  8,  9, 10, 11]])


arr3.reshape(4,3)
#O/P:- array([[ 0,  1,  2],
#        [ 3,  4,  5],
#        [ 6,  7,  8],
#        [ 9, 10, 11]])
#

arr3.reshape(3,4)
#O/P:- array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])



arr3.reshape(3,4) # (rows,col) : rows * coln = total no of elements =  size of the array
#O/P:- array([[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])



arr3.reshape(6,2)
# array([[ 0,  1],
#        [ 2,  3],
#        [ 4,  5],
#        [ 6,  7],
#        [ 8,  9],
#        [10, 11]])



arr3.reshape(1,12)
# array([[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11]])



arr3.reshape(12,1)
# array([[ 0],
#        [ 1],
#        [ 2],
#        [ 3],
#        [ 4],
#        [ 5],
#        [ 6],
#        [ 7],
#        [ 8],
#        [ 9],
#        [10],
#        [11]])



arr3.dtype  #dtype('int32')



arr4 = np.linspace(1,10,15)
arr4.reshape(5,3)
# array([[ 1.        ,  1.64285714,  2.28571429],
#        [ 2.92857143,  3.57142857,  4.21428571],
#        [ 4.85714286,  5.5       ,  6.14285714],
#        [ 6.78571429,  7.42857143,  8.07142857],
#        [ 8.71428571,  9.35714286, 10.        ]])



# reshaping the array in single command
arr4 = np.linspace(1,10,15).reshape(5,3)
arr4
# array([[ 1.        ,  1.64285714,  2.28571429],
#        [ 2.92857143,  3.57142857,  4.21428571],
#        [ 4.85714286,  5.5       ,  6.14285714],
#        [ 6.78571429,  7.42857143,  8.07142857],
#        [ 8.71428571,  9.35714286, 10.        ]])


arr4.dtype          #dtype('float64')


b  = [1,2,3,4,'a','b','c','d']
arr5 = np.array(b)
print(arr5)
# ['1' '2' '3' '4' 'a' 'b' 'c' 'd']



arr5
# array(['1', '2', '3', '4', 'a', 'b', 'c', 'd'], dtype='<U11')



arr5.dtype      # dtype('<U11')


arr3.shape      #(12,)


# If one unknown dimension
arr3.reshape(6,-1) # shape  =  12 , rows = 6 ,coln  = ? : if one of the values is dummy , it will be calculated and replaced by numpy
# array([[ 0,  1],
#        [ 2,  3],
#        [ 4,  5],
#        [ 6,  7],
#        [ 8,  9],
#        [10, 11]])




arr3.reshape(-6,2)
# array([[ 0,  1],
#        [ 2,  3],
#        [ 4,  5],
#        [ 6,  7],
#        [ 8,  9],
#        [10, 11]])


arr3.reshape(-6,-3)
#O/P:- ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# Input In [45], in <cell line: 1>()
# ----> 1 arr3.reshape(-6,-3)
#
# ValueError: can only specify one unknown dimension
