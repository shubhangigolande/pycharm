class A:
    def method(self):
        print("A's method is called")

class B(A):
    def method(self):
        print("B 's method is called")

class C(A):
    def method(self):
        print("C 's method is called")

class D(B,C):
    pass

d = D()
d.method()


# overloading


# class Cal:
#     def add(self ,x,y):
#         print(x+y)
#
#     def add(self,x,y,z):
#         print(x+y+z)
#
#     def add(self,x,y,z,a):
#         print(x+y+z+a)
#
# a = Cal()
# a.add(12,45,4,5)

class Cal:
    def add(self , a = None , b = None , c = None , d = None):
        if(a != None and b != None  and c != None and d != None):
            print(a+b+c+d)
        elif(a != None and b != None and c != None):
            print(a+b+c)
        elif(a != None and b != None):
            print(a + b)

a = Cal()
a.add(12,14,4,5)
a.add(12,14,4)
a.add(12,14)