def calc(a,b):
    print(a+b)    #136
    print(a-b)    #-10
calc(63,73)



def calc(a,b):
    print(a+b)
    print(a-b)
calc()
---------------------------------------------------------------------------
#  O/P:= TypeError                                 Traceback (most recent call last)
# Input In [3], in <cell line: 4>()
#       2     print(a+b)
#       3     print(a-b)
# ----> 4 calc()
#
# TypeError: calc() missing 2 required positional arguments: 'a' and 'b'



#List as an argument
# to filter even number from the given list
a = [10,11,12,13,44,15]
b = []
for i in a:
    if i%2 == 0:
        #         print("The number is even")
        b.append(i)
    print(b)     #[10, 12, 44]

    # print(14%2)



    def even_filter(a):
        b = []
        for i in a:
            if i % 2 == 0:
                #         print("The number is even")
                b.append(i)
        print(b)   #[2, 4, 6, 8]  #[]

    even_filter([1, 2, 3, 4, 5, 6, 7, 8, 9])
    even_filter([3, 9, 19, 23])




    # varable lenght argument
    # args
    # *args
    def sum(a, b, c):
        print(a + b + c)
    sum(10, 20, 30)   #60





    def sum(a, b, c=0, d=0, e=0, f=0):
        print(a + b + c + d)
    sum(10, 20)    #30
    sum(10, 20, 30)     #60
    sum(10, 20, 30, 40)      #100




    def sum(*args):
        sum = 0
        for i in args:
            #         print(i)
            sum = sum + i
        print(sum)

    sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, -17)    #119
    sum(-17)      #-17
    sum(0, -17)     #-17
    sum(17, -17)    #0
