# inbuilt module in Python
# no need to download or install

#  import Name_of_module
import os


# getting help
# help(os) #manual pages
# dir(os


# checking the current location
# current working directory of exisiting dir
os.getcwd()
#O/P:- 'C:\\Users\\RAHUL\\Documents\\OnePython\\013. JULY_DS_8.30AM_9PM


# changin the directory
os.chdir(r'D:\New folder')


os.getcwd()
#O/P:- 'D:\\New folder'


# making a new directory
os.mkdir("demo2")



# changin the dir to required one
os.chdir(r"D:\New folder\demo2")



os.getcwd()
# O/P:- 'D:\\New folder\\demo2'



# creating dir using for loop
for i in range(2,11):
    os.mkdir(f"Emp{i}")



os.rmdir('Emp10/')

os.getcwd()
#O/P:- 'D:\\New folder\\demo2'



os.rmdir('demo2')
#O/P:- ---------------------------------------------------------------------------
# FileNotFoundError                         Traceback (most recent call last)
# Input In [28], in <cell line: 1>()
# ----> 1 os.rmdir('demo2')
#
# FileNotFoundError: [WinError 2] The system cannot find the file specified: 'demo2'




os.listdir(r'D:\New folder\demo2')      #O/P:= ['Emp1', 'Emp2', 'Emp3', 'Emp4', 'Emp5', 'Emp6', 'Emp7', 'Emp8', 'Emp9']

os.chdir(r'D:\New folder')

os.listdir(r'D:\New folder')    #O/p:-['demo1', 'demo2']



os.rmdir('demo2/') # dir have data , so python will not allow to delete
#O/P:- ---------------------------------------------------------------------------
# OSError                                   Traceback (most recent call last)
# Input In [35], in <cell line: 1>()
# ----> 1 os.rmdir('demo2/')
#
# OSError: [WinError 145] The directory is not empty: 'demo2/'




os.rmdir('demo1/')

os.remove('demo2/')
#O/P:- ---------------------------------------------------------------------------
# PermissionError                           Traceback (most recent call last)
# Input In [37], in <cell line: 1>()
# ----> 1 os.remove('demo2/')
#
# PermissionError: [WinError 5] Access is denied: 'demo2/'



os.removedirs('demo2/')
#O/P:- ---------------------------------------------------------------------------
# OSError                                   Traceback (most recent call last)
# Input In [38], in <cell line: 1>()
# ----> 1 os.removedirs('demo2/')
#
# File C:\Python\Python310\lib\os.py:243, in removedirs(name)
#     232 def removedirs(name):
#     233     """removedirs(name)
#     234
#     235     Super-rmdir; remove a leaf directory and all empty intermediate
#    (...)
#     241
#     242     """
# --> 243     rmdir(name)
#     244     head, tail = path.split(name)
#     245     if not tail:
#
# OSError: [WinError 145] The directory is not empty: 'demo2/'




help(os.removedirs)
#O/P:- Help on function removedirs in module os:
#
# removedirs(name)
#     removedirs(name)
#
# Super-rmdir; remove a leaf directory and all empty intermediate
#     ones.  Works like rmdir except that, if the leaf directory is
#     successfully removed, directories corresponding to rightmost path
#     segments will be pruned away until either the whole path is
#     consumed or an error occurs.  Errors during this latter phase are
#     ignored -- they generally mean that a directory was not empty.





os.getcwd()     #O/P:-'D:\\New folder'

os.chdir(r"D:\New folder\demo2")

os.listdir()        #O/P;['Emp1', 'Emp2', 'Emp3', 'Emp4', 'Emp5', 'Emp6', 'Emp7', 'Emp8', 'Emp9']


# removing multiple dir usiing for loop
for i in os.listdir():
    os.rmdir(i)
os.listdir()        #O/P:- []











