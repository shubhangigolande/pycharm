#################################################
#  22.07.2023 8.30AM
#################################################
#  TOPICS TO BE COVERED
# 👉 for loop
# 👉 range()
#################################################
#                   0        1       2        3        4        5
students_pass = ['Ramesh', 'Akash', 'Pratik', 'Pranav', 'Sunita', 'Sneha']
print(students_pass)
print(len(students_pass))
print(students_pass[0])
print(students_pass[1])
print(students_pass[2])
print(students_pass[3])
print(students_pass[4])
print(students_pass[5])

# Syntax
# for i in iterable:
#   code

print("***************")

for students in students_pass:
    print(students)

email_id = "minskole@gmail.com"
print(email_id[0])
print(email_id[1])

for i in email_id:
    print(i)

print("***************")
list_even = [2, 4, 6, 8, 10, 12]
print(list_even[0] * 2)
print(list_even[1] * 2)
print(list_even[2] * 2)
print(list_even[3] * 2)

# taking double
for i in list_even:
    print(i * 2)

# taking square
for i in list_even:
    print(i * i)