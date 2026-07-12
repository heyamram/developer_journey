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
print(4==(8/2) and 8 > 5 and 1.1==1)
print(5!=5 or 6.0>6 or (2**2)==4)