""" Q.1. Print table of user choice"""





"""Q.2 check leap year of user choice"""


"""Q.3 Sum of n term"""


"""Q.4 Count all odd and even till user want"""


"""Q.5 Print sum of all even and odd no up to user wants seperaately"""

        
"""Q.6 Factorial of a number of user choice"""


"""Q.5 user want to know the the factors of their no """


"""Q.6 user want to know, how many facors their no has"""


""" Q.7 user want to check the the no is perfect or not"""


""" Q.8 check the user no is prime or not"""


""" Q.9 check user string is pallindrome or not """

    
""" Q.9 user want to seprate digit of their number"""


""" Q.10 check user number is pallindrome or not """


"""" Q.11 count all leters, digits and special char in user string"""


"""""""while loop question"""""""

""" Q.12 print number from 10 to 15"""


""" Q.13 print cube of nuber form 1 to 10"""


""" Q.14 print odd and even no. from 1 to 10"""


""" Q.15 user want to know factorial"""


""" Q.16 user want to reverse his word"""


""" Q.17 reverse each word in sentence given by user"""


""" Q.18 user wants to count vowerls and consonents in word """


""" Q.19 user want to know which consonents and how many times comes in his stings"""


""" Q.20 User print first five multiple of his number """


""" Q.21 user want to calculate power of his number """


""" Q.22 user want check his number is perfect square or not"""


""" Q.23 print fibbonacci sequence upto n term """


""" Q.24 Give occerence of each character in the string"""


""" Q.25 make a fun to check sting is pallindromic or not"""


""" Q.26 write a python script to merge two python dictionaries """
d1 = {10:100,20:200,40:300}
d2 = {40:400,50:500,60:600}
# d1.update(d2)                     # m1
# print(d1)

# for i in d2:                      # m2
#     d1[i] = d2[i]
# print(d1)

""" Q.27 write a python program to sum all the values in a dictionary """
# sum = 0
# for i in d1:
#     sum += d1[i]
# print(sum)

""" Q.28 count the frequency of each elements in list[1,1,1,1,2,2,2,3,3,3,4,4,5] """
# l = [1,1,1,1,2,2,2,3,3,3,4,4,5]
# d = {}
# for i in l:                     
#     if i in d.keys():
#         d[i] +=1 
#     else:
#         d[i] = 1
# print(d)

# dry run 
# picked 1 then else run becoz dict is empty -> d[1] = 1
# picked 1 then if run becoz key 1 is present -> d[1] = 1+1= 2
# picked 1 then if run becoz key 1 is present -> d[1] = 2+1=3
# picked 1 then if run becoz key 1 is present -> d[1] = 3+1=4
# picked 2 then else run becoz 2 not present in key -> d[2] = 1
# picked 2 then if run becoz now 2 is present in key so -> d[2] = 3
# finally d updated like we study "updae" in CRUD -> {1: 4, 2: 3, 3: 3, 4: 2, 5: 1}

""" Q.30 write a python program to combine two dictionary by adding values for common keys """
# d1 = {10:100,20:200,40:300}
# d2 = {40:400,50:500,60:600}
# for i in d2:
#     if i in d1.keys():
#         d1[i] += d2[i]
#     else:
#         d1[i] = d2[i]
# print(d1)


