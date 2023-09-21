# revision
# 2D Array creation
# using aranage() and reshape()

import numpy as np

x = [[1,2,3],[3,4,5]]
arr1 = np.array(x)
print(arr1)
# [[1 2 3]
#  [3 4 5]]


print(list(range(10)))
print(list(range(1,10,2)))
print(np.arange(10))
print(np.arange(1,10,0.5))
#O/P:- [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 3, 5, 7, 9]
# [0 1 2 3 4 5 6 7 8 9]
# [1.  1.5 2.  2.5 3.  3.5 4.  4.5 5.  5.5 6.  6.5 7.  7.5 8.  8.5 9.  9.5]




arr2 = np.arange(1,10,0.5)
arr2.ndim       # 1


arr2.shape          #  (18,)


arr2.size       #18


arr2.dtype      # dtype('float64')


arr2.reshape(2,9)
# array([[1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5, 5. ],
#        [5.5, 6. , 6.5, 7. , 7.5, 8. , 8.5, 9. , 9.5]])


arr2.reshape(9,2)
# array([[1. , 1.5],
#        [2. , 2.5],
#        [3. , 3.5],
#        [4. , 4.5],
#        [5. , 5.5],
#        [6. , 6.5],
#        [7. , 7.5],
#        [8. , 8.5],
#        [9. , 9.5]])



arr2.reshape(1,18) #column vector
# array([[1. , 1.5, 2. , 2.5, 3. , 3.5, 4. , 4.5, 5. , 5.5, 6. , 6.5, 7. ,
#         7.5, 8. , 8.5, 9. , 9.5]])



arr2.reshape(18,1) #row vector
# array([[1. ],
#        [1.5],
#        [2. ],
#        [2.5],
#        [3. ],
#        [3.5],
#        [4. ],
#        [4.5],
#        [5. ],
#        [5.5],
#        [6. ],
#        [6.5],
#        [7. ],
#        [7.5],
#        [8. ],
#        [8.5],
#        [9. ],
#        [9.5]])


arr2.reshape(9, -2)
# array([[1., 1.5],
#        [2., 2.5],
#        [3., 3.5],
#        [4., 4.5],
#        [5., 5.5],
#        [6., 6.5],
#        [7., 7.5],
#        [8., 8.5],
#        [9., 9.5]])



arr2.reshape(-9, -2)
# O/P:----------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# Input In [23], in <cell line: 1>()
# ----> 1 arr2.reshape(-9,-2)
#
# ValueError: can only specify one unknown dimension


