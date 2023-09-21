import numpy as np

a1 = [1,2,3,4,5,6,7]
a1  # [1, 2, 3, 4, 5, 6, 7]

arr1 = np.array([1,2,3,4,5,6,7])
arr1    # array([1, 2, 3, 4, 5, 6, 7])

# array supports elementwise operation

print(type(arr1))   #<class 'numpy.ndarray'>

# 1D Array

print(arr1.ndim)    # 1
print(arr1.shape) # (x_axis,y_axis) (0th,1st) (rows,coln)   # O/P:-  (7,)


print(arr1.size) #total number of elements inside the array     # 7


arr2 = np.array(['A', 'B', 'C', 'D', 'E', 'F'])
arr2        # array(['A', 'B', 'C', 'D', 'E', 'F'], dtype='<U1')


# attributes of arr2
# dim
print(arr2.ndim)
# shape
print(arr2.shape)
# size
print(arr2.size)
# O/P:-# 1
# (6,)
# 6


# 1D Array creation
# by passing a list
# using arange() method
# using linspace
list(range(10)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list(range(1,10)) #last ement is not included # O/P:- [1, 2, 3, 4, 5, 6, 7, 8, 9]

list(range(1,10,2))     #[1, 3, 5, 7, 9]

list(range(1,10,0.5))       #O/P:----------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# Input In [26], in <cell line: 1>()
# ----> 1 list(range(1,10,0.5))
# TypeError: 'float' object cannot be interpreted as an integer


arr3 = np.arange(10)
arr3        # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


arr3 = np.arange(1,10)#last ement is not included
arr3        # array([1, 2, 3, 4, 5, 6, 7, 8, 9])


arr3 = np.arange(1,10,2)
arr3        # array([1, 3, 5, 7, 9])


arr3 = np.arange(1,10,0.5)#step size in fraction is allowed in aranage() method
arr3         #array([1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5, 5. , 5.5, 6. , 6.5, 7. ,7.5, 8. , 8.5, 9. , 9.5])




# attributes of arr2
# dim
print(arr3.ndim) #1D
# shape
print(arr3.shape) #(x,y) > (18,)
# size
print(arr3.size)#
#O/P:-  1
# (18,)
# 18


# using linspace
arr4 = np.linspace(1,10,18) #the element is included
arr4
#O/P:-  array([ 1.        ,  1.52941176,  2.05882353,  2.58823529,  3.11764706,
#         3.64705882,  4.17647059,  4.70588235,  5.23529412,  5.76470588,
#         6.29411765,  6.82352941,  7.35294118,  7.88235294,  8.41176471,
#         8.94117647,  9.47058824, 10.        ])



# attributes of arr2
# dim
print(arr4.ndim) #1D
# shape
print(arr4.shape) #(x,y) > (18,)
# size
print(arr4.size)#
#O/P:-# 1
# (18,)
# 18



# using linspace
arr4 = np.linspace(1, 10, 19)  # the element is included
arr4        #O/P:-  array([1., 1.5, 2., 2.5, 3., 3.5, 4., 4.5, 5., 5.5, 6.,6.5, 7., 7.5, 8., 8.5, 9., 9.5, 10.])




