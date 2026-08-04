print("hi myself ram_narayan")
"""
RamNarayan = pascle case
ram_narayan = snake case
ramNarayan = camel case

python = interpreter (virtual machine)
ide = (integrated virtual environment) - vscode,pycharm,jupyter
"""
# in string every character has unicode becoz character takes more space
# print(ord("A"))
# print(chr(65))

"""string indexing"""
# a = "heyamram"
# print ((a[5]),(a[7]))    start counting with zero

"""string slicing"""
# a = "heyamram"
# print(a[5::])  a[start:stop:steps]   
# print(a[::]).    by default [o:end:1]

"""type conversion"""
# a = 12               int
# b = "ram123!@#$"     str
# c = 1.5              float
# d = True             bool
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(str(a)))     we can convert str to int but not vice versa

# bool is interesting, if we convert anything to bool give True
# except - False, 0, 0.0, " ", ( ), [ ], { } --> these are falsy 
# print(bool("ram"))
# print(bool(0))   

# explicit - like we are doing
# implicit - like python do automatically to 4/3 float

"""input and output"""
# name = input("Hello what is your name :-")
# age = input("also your is :-")
# print("good morning", name, "your age is",age)
# print(f"good morning {name},your are {age} years old")

"""logical operator, in and both true - true, in or both false - false"""
# print(4==(8/2) and 8 > 5 and 1.1==1)
# print(5!=5 or 6.0>6 or (2**2)==4)

""" loop"""
# for i in range(1,21,1):      # for loop work in a range
#     print(i, end= ",")

# a = 1
# while a <= 20:
#     print(a, end= " ")
#     a += 1


"""in sting for_loops"""
# a = "heyamram"
# by index 
# print(a[7])
# print(a[::])      [start:end:steps]

# direct by for loops
a = "ram is a programmer"
# for i in a:
#     print(i, end= "")

# for i in range(len(a)):
#     print(a[i], end= "")

""" Break and continue """
# for i in range(1,21):
#     if i == 15:
#         break
#     else:
#         print(i, end= " ")        # if i = 15 then loop break, print till 14

# for i in range(1,21):
#     if i == 15:
#         continue
#     print(i, end=" ")            # here i = 15 ko skip kar ke loop continue rakhega

""" function """
# def fun_name():
#     print("Hello Dhruv, How are you?")

# fun_name()

""" ex.1 """
# def add(a,b):
#     print(f"the sum of {a} and {b} is {a+b}")

# add(5,6)                # positional argument
# add(b = 5, a = 6)       # keyword argument

""" ex.2 """
# def introduce(name, age):
#     print(f"Hello i am {name} and my age is {age}")

# introduce("Dhruv", 7)
# introduce(age = 29, name = "Ram")

""" ex.3 """
# def greet(guest = "Sir"):
#     print(f"Good Morning {guest}")

# greet()                   # default argument
# greet("Dhruv")

""" use of return """
# we use return when we don't want to write print in function
# def hello():
#     return "hello how are you mam"

# print(hello())

""" data structure
________________________________________________________________________
------------------------------------------------------------------------"""
#                 list        tuple       set         dict
# mutable          yes        no          yes         yes
# duplicates       yes        yes         no          no
# order            yes        yes         no          yes(insertion order)
# heterogeneou     yes        yes         semi        yes
# Structure        [ ]        ( )         { }         {k:v}

""" list method """
# l = [4,5,7,3,8,7]
# l.append(9)             # add 9 to last
# l.extend([10,11,12])    # add multiple object
# l.insert(1,8)           # insert 8 at index 1 
# l.remove(5)             # remove pahle aane wala 5
# l.sort()                # in ascending order
# l.clear()               # remove all object
# l.reverse()             # reverse the list
# n = l.count(7)          # count all 7 present in the list
# print(n)
# n = l.pop(2)            # remove and store who is at index 2 
# print(n)
# print(l)                 

""" tuple has only two method """
# t = (9,8,5,2,6,7,5,3)
# print(t.index(6))
# print(t.count(5))

""" set """         #value stored in set in hashing form
# a = {2,3,4}
# b = {4,5,6}

# union = a.union(b)                      #(2,3,4,5,6)
# intersection = a.intersection(b)        #(4)
# difference = a.difference(b)            #(2,3)
# sym_diff = a.symmetric_difference(b)    #(2,3,5,6)

# print(a | b)          # union = show all element once
# print(a & b)          # intersection = only common element
# print(a - b)          # difference = a me se wo element minus kar dena jo b me bhi present h
# print(a ^ b)          # symmetric diff = dono me jo common hai use hata dena 

""" Dictionary """  

# d = {1:"ram", 2:29, 3:5.2}
# print(d[2])                 # we can access value through key like we use index in list

# d[1] = "nishu"              
# print(d)                    # update - only value inside key is mutable not key

# d.update({4:"coder"})       # create or d[4] = "coder" 
# print(d)

# del d[3]                    # delete using key
# print(d)

# for i in d:
#     print(i)                # print key
#     print(d[i])             # print value

# for i in d.values():        # directly access value
#     print(i)

""" dict method """

# f = d
# f[1] = "dhruv"
# print(d)                # reference assignment, updae occur in both d & f

# f = d.copy()
# f[1] = "dhruv"
# print(d)                # shallow copy, only updae in f not in d
# print(f)

""" Exception handling """
# syntax and indentation error we can't handle

# a = int(input("tell your number :- "))
# print(10/a)                             # if a=0 then raise zero division error
# print("my task end")                    # and this will not excuted and progamme stopped here

""" try and except are most commonly used """
# try:
#     print(10/a)
# except ZeroDivisionError:                         # if we know errror
#     print("sorry you cannot divide by zero")

# except Exception as err:                          # if we don't know whivh error about to come
#     print(f"sorry there is an error as {err}")

""" try except else finally """
# try:
#     print(10/a)
# except Exception as err:                          # if we don't know whivh error about to come
#     print(f"sorry there is an error as {err}")
# else:
#     print("good no error found")
# finally:
#     print("i will continue running code no matter what")

""" raise -> we raise error not python programme """

# age = int(input("tell your age :- "))
# try:
#     if age < 10 or age > 18:
#         raise ValueError("your age must be between 10 and 18")
#     else:
#         print("welcome to the club")
# except Exception as err:
#     print(f"an error arises as {err}")

# print("your code will continue running")

""" File Handling -> CRUD in files , also check the project """
# p = open('python/basic.py')
# print(p.read())

# file = open("dhruv.txt","w")       # create or overwrite
# file.write("hello i am dhruv and i am a class 1 student. ")
# file.close()

# file = open("dhruv.txt","a")       # apppend
# file.write("i live in khemnichak patna.")
# file.close()

# file = open("dhruv.txt","r")       # read by default, we can also add "r"
# print(file.read())             # read all content
# file.close()

""" OOPS (OBJECT ORIENTED PROGRAMMING SYSTEM)"""
# # imperative approach
# a = 4
# b = 5
# print(a+b)

# # functional approach
# def add(a,b):
#     print(a+b)
# add(4,5)

# oops approach
""" classes in oops -> has two things - attribute(variable) and method(function) """
# class Factory:
#     a = 2                   # attribute (just like variable)
#     def greet(self):        # method (just like function)
#         print("welcome to the Factory")

# print(Factory().a)
# Factory().greet()

# obj = Factory()
# obj2 = Factory()

""" example """
# class Factory:
#     def __init__(self,material,zips,pockets):    # self targets object location
#         self.material = material                 # reebok.material = leather
#         self.zips = zips                         # reebok.zips = 2
#         self.pockets = pockets
    
#     def show(self):
#         print(f"your object details are {self.material}, {self.zips}, {self.pockets}")

# reebok = Factory("leather",2,3)
# campus = Factory("nylon",3,3)
# skybags = Factory("fabric",2,2)

# print(campus.pockets)
# print(reebok.material)

# reebok.show()                   # this calls show fun
# campus.show()
# skybags.show()

""" methods in oops """
# class Animalia:
#     name = "lion"                                #class attribute
        
#     def __init__(self,age,location):
#         self.age = age 
#         self.location = location                 #instance attribute
        
#     def show(self):                              # instance method target object
#         print(f"lion age is {self.age} and he lived in {self.location}.")
        
#     @classmethod
#     def hello(cls):                              # here cls target class animal not object
#         print("your class is animalia")

#     @staticmethod
#     def static():
#         print("how are you lion")    

# obj = Animalia(12, "zoo")
# obj.show()
# obj.hello()
# obj.static()