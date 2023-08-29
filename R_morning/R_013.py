#################################################
#  17.07.2023 9.00AM
#################################################
#  TOPICS TO BE COVERED
# 👉 Operators in Python
#################################################


'''
Control flow in Python required understanding of
> Operators
> Boolean interpretation of the statements True/False

'''

''' 
1. Arithmetic Operators:
   - Addition (+)
   - Subtraction (-)
   - Multiplication (*)
   - Division (/)
   - Modulo (%)
   - Exponentiation (**)
   - Floor Division (//)

2. Assignment Operators:
   - Assignment (=)


3. Comparison Operators:
   - Equal to (==)
   - Not equal to (!=)
   - Greater than (>)
   - Less than (<)
   - Greater than or equal to (>=)
   - Less than or equal to (<=)

4. Logical Operators:
   - AND (and)
   - OR (or)
   - NOT (not)

5. Bitwise Operators:
   - Bitwise AND (&)
   - Bitwise OR (|)
   - Bitwise XOR (^)
   - Bitwise NOT (~)
   - Left Shift (<<)
   - Right Shift (>>)

6. Membership Operators:
   - In (in)
   - Not in (not in)

7. Identity Operators:
   - is
   - is not

'''

# Assignment Operators:

x = 100 # Assignment operation


# Comparison Operators:
x == 100 #comparison

print(x == 100) #True
a = 55
b = 65

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)



# Logical Operators:


a = 55
b = 65

x = 100
y = 200

# and
print((a>b) and (x<y))
print((a<b) and (x<y))


# or

print((a>b) or (x<y))
print((a<b) or (x<y))
print((a>b) or (x>y))

# NOT
#  will negate the output

print(not((a>b) or (x>y)))