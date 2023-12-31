#################################################
#  28.07.2023 8.30AM
#################################################
#  TOPICS TO BE COVERED
# 👉 Dictionary in Python
#################################################
# Intro to Dictionary

# requirement of dict ?


students  = ['samir','saket','sanjeev','suresh']
marks = [75,74,81,42]

print(students)
print(students[0])
print(students[1])
print(students[2])

print(students[0])
print(marks[0])


print(students[1])
print(marks[1])


# creating a Dictionary
# var_name = {key1: value1,key2:value2 }
# keys behave like customized indexes
# is used to access the value corresponding to the key

student_info = {
  'samir' : 75,
  'saket' : 74,
  'sanjeev': 81,
  'suresh' : 42
}

print(student_info)
print(type(student_info))


student_info1 = {} #creating an empty Dictionary
print(type(student_info1))


student_info1 = {" "} # this contains a single element , its a set
print(type(student_info1))


student_info1 = {" ": " "} #key : value pair , so its a Dictionary
print(type(student_info1))

# accessing the Dictionary using []


print(student_info['samir'])
print(student_info['sanjeev'])
print(student_info['suresh'])


# accessing the Dictionary using dot notation
print(student_info.get('samir'))