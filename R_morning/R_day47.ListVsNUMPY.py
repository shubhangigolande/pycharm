a1 = [1,2,3,4,5,6,7,8,9,10]
print(a1)   #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# to get the sq of every element in the list
# a1*a1     #O/P:- ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# Input In [2], in <cell line: 2>()
#       1 # to get the sq of every element in the list
# ----> 2 a1*a1
#
# TypeError: can't multiply sequence by non-int of type 'list'



# using for loop
for i in a1:
    print(i*i)
#O/P:- 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100





# using list comprehension
a2 = [i*i for i in a1]
a2   #O/P:- [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]



import numpy as np

# converting the list into array
print(a1)
print(type(a1))
arr1 = np.array(a1)
print(arr1)
print(type(arr1)) #ndarray  : n dim array
#O/P:- [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# <class 'list'>
# [ 1  2  3  4  5  6  7  8  9 10]
# <class 'numpy.ndarray'>




5**2        #25


5**3        #125


print(arr1**2)      #[  1   4   9  16  25  36  49  64  81 100]


arr1**2     #array([  1,   4,   9,  16,  25,  36,  49,  64,  81, 100])


# 1. can perform elementwise operations
# 2. faster than list operations

a1  = list(range(100000))

% timeit [i*i for i in a1]            # 8.37 ms ± 357 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

# usin NUmpy
arr2  = np.array(a1)
% timeit (arr2**2)       #98.8 µs ± 3.57 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)



# why faster ? it is  written C language

