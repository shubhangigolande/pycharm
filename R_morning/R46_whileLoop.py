WHILE loop
#WHILE loop

# syntax
# while expression/condition:
#     code

for i in range(5):
    print("I will attend the class daily")
#O/P:- I will attend the class daily
# I will attend the class daily
# I will attend the class daily
# I will attend the class daily
# I will attend the class daily




# below colde will lead to infinite no of executions , infinite loop
# while 1 <5:
#     print("I will attend the class daily")



# eg:

i=0 #variable initialization
while i <5: #loop will be exited when the value of i becomes 5
    print("I will attend the class daily", i)
    i=i+1 #expression which will make the while statment out of loop
#O/P:- I will attend the class daily 0
# I will attend the class daily 1
# I will attend the class daily 2
# I will attend the class daily 3
# I will attend the class daily 4


# eg: reoredering the increment code

i = 0  # variable initialization
while i < 5:  # loop will be exited when the value of i becomes 5
    i = i + 1  # expression which will make the while statment out of loop
    print("I will attend the class daily", i)
#O/P:- I will attend the class daily 1
# I will attend the class daily 2
# I will attend the class daily 3
# I will attend the class daily 4
# I will attend the class daily 5




# use of while loop !!!
# > the number of repetations is unknkown




while True:
    user_input =  input("Press 'q' to quit the game")
    if user_input == 'q':
        break
#O/P:- Press 'q' to quit the gamez
# Press 'q' to quit the gamea
# Press 'q' to quit the game1
# Press 'q' to quit the gamequit
# Press 'q' to quit the gameescape
# Press 'q' to quit the gameq




while True:
    user_input =  input("Press 'q' to quit the game")
    if user_input == 'q':
        break
#O/P:- Press 'q' to quit the gameq




while True:
    user_input =  input("Press 'q' to quit the game")
    if user_input == 'q':
        break
# O/P:-# Press 'q' to quit the game1
# Press 'q' to quit the game1
# Press 'q' to quit the game1
# Press 'q' to quit the game1
# Press 'q' to quit the game1
# Press 'q' to quit the game1
# Press 'q' to quit the game1
# Press 'q' to quit the game
# Press 'q' to quit the game1
# Press 'q' to quit the game1
# Press 'q' to quit the game1
# Press 'q' to quit the game1
# Press 'q' to quit the gameq





#eg:

valid_input = False
while not valid_input:

    value = input("Enter a number!!")
    if value.isdigit():
        print("value entered is a digit")
        valid_input = True
    else:
        print("invalid value entered")
# O/P:-# Enter a number!!one
# invalid value entered
# Enter a number!!two
# invalid value entered
# Enter a number!!3
# value entered is a digit
