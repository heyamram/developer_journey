""" Q.1. Print table of user choice"""
# n = int(input("which table you want to learn today? :-"))
# for i in range (n, (n*10)+15, n):
#     print(i)

# for i in range(1,11):
#     print(f"{n} * {i}= {n * i}")

""" Q.1. Print table of user choice """

# while True:
#     try:
#         # Added spaces for readability and a space at the end of the prompt
#         n = int(input("Which table do you want to learn today? : "))
#         break # Exits the loop if the input was a valid integer
#     except ValueError:
#         print("Invalid input. Please enter a whole number.")

# for i in range(1, 11):
#     # Added spaces inside the f-string for cleaner terminal output
#     print(f"{n} * {i} = {n * i}")

"""Q.2 check leap year of user choice"""
# lp = int(input("which year you want to check :-"))
# if (lp % 100 == 0 and lp % 400 == 0) or (lp % 100 != 0 and lp % 4 == 0):
#     print(f"{lp} is a leap year")
# else:
#     print(f"{lp} is not a leap year")

"""Q.3 Sum of n term"""
# n = int(input("you want to add up to :-"))
# sum = 0
# for i in range(1,(n+1)):
#     sum += i
# print(f"sum up to {n} is {sum}")

"""Q.4 Count all odd and even till user want"""
# n = int(input("tell me your no. :-"))
# even = 0
# odd = 0
# for i in range(1,(n+1)):
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(f"there are {even} even and {odd} odd")

"""Q.5 Print sum of all even and odd no up to user wants seperaately"""
# n = int(input("you want to add up to : "))
# even = 0
# odd = 0
# for i in range(1,(n+1)):
#     if i % 2 == 0:
#         even += i
#     else:
#         odd += i
# print(f"sum of all even is {even} and all odd id {odd}")
        
"""Q.6 Factorial of a number of user choice"""
# n = int(input("tell me the no : "))
# fact = 1
# for i in range(1,(n+1)):
#     fact *= i
# print(f"the factorial of ypur no. is {fact}")

"""Q.5 user want to know the the factors of their no """
# n = int(input("tell mw which no. factor you want : "))
# for i in range(1,(n+1)):
#     if n % i == 0:
#         print(i)

"""Q.6 user want to know, how many facors their no has"""
# n = int(input("tell me the no : "))
# factor = 0
# for i in range(1,(n+1)):
#     if n % i == 0:
#         factor += 1
# print(f"the no.{n} has {factor} factors")

""" Q.7 user want to check the the no is perfect or not"""
# n = int(input("tell me your no "))
# sum = 0
# for i in range(1,n):
#     if n % i == 0:
#         sum += i
# if sum == n:
#     print(f"your no. {n} is a perfect no")

""" Q.8 check the user no is prime or not"""
# n = int(input("tell me your no "))
# sum = 0
# for i in range(1,(n+1)):
#     if n % i == 0:
#         sum += 1
# if sum == 2:
#     print(f"yor no. {n} is a prime no.")
# else:
#     print(f"yor no. {n} is not a prime no.")

""" Q.9 check user string is pallindrome or not """
# n = input("tell me your str : ")
# reverse = ""
# for i in range((len(n) - 1),-1,-1):   # here first we find index of last digit by len() then we se range
#     reverse += n[i]                   # if we print here then reverse str has been printed
# if reverse == n:
#     print("your str is pallindromic")
# else:
#     print("your str is not pallindromic")

"""m2"""
# n = input("tell me your str : ")
# if n == n[::-1]:
#     print("your str is pallindromic")
# else:
#     print("your str is not pallindromic")
    
""" Q.9 user want to seprate digit of their number"""
# n =(input("tell me your no "))
# for digit in n:
#     print(digit)                     # here if keep number in string then we easily print

# n = int(input("tell me your no "))
# while n > 0:
#     print(n % 10)                    # here is just print from last to first line by line
#     n //= 10                         # if we want to print first to last then first reverse it

# n = int(input("tell me your no "))
# while n > 0:
#     print(n % 10, end= "")           # here it print in revrse order in a single line
#     n //= 10





""" Q.10 check user number is pallindrome or not """
# n = int(input("tell me your no "))
# rev = 0
# copy = n
# while n > 0:
#     rev = (rev * 10) + (n % 10)
#     n //= 10      # here we print reverse of our number
# if rev == copy:
#     print("your no. is pallindromic")
# else:
#     print("your no. is not pallindromic")

"""" Q.11 count all leters, digits and special char in user string"""
# a = input("tell me your str : ")
# letter = 0
# digit = 0
# spchr = 0
# for i in a:
#     if i.isdigit():      .isdigit is inbild fun
#         digit += 1
#     elif i.isalpha():
#         letter += 1
#     else:
#         spchr += 1
# print(f"your string has :-\n{letter} letters\n{digit} digits\n{spchr} special character")


"""""""while loop question"""""""

""" Q.12 print number from 10 to 15"""
# num = 10
# while num <= 15:
#     print(num, end=" ")
#     num += 1

""" Q.2 print cube of nuber form 1 to 10"""
# num = 1
# while num <= 10:
#     print(num ** 3, end=",")
#     num += 1

""" Q.3 print odd and even no. from 1 to 10"""
# num = 1
# print("even numbers are :- " )
# while num <= 10:
#     if num % 2 == 0:
#         print(num, end = ",")
#     num += 1
# print("\nodd numbers are :- " )
# num = 1
# while num <= 10:
#     if num % 2 == 1:
#         print(num, end = ",")
#     num += 1

""" m2 """
# num = 1
# even = ""
# odd = ""
# while num <=10:
#     if num % 2 == 0:
#         even += f"{num},"
#     else:
#         odd += f"{num},"
#     num += 1
# print(f"even numbers are :- {even}")
# print(f"even numbers are :- {even}")

""" Q.4 user want to know factorial"""
# num = int(input("tell me your number :- "))
# n = 1
# fact = 1
# while n <= num:
#     fact *= n
#     n += 1
# print(f"the factorial of {num} is {fact}")

""" Q.5 user want to reverse his word"""
"""m1"""
# word = input("enter the word you want to reverse :- ")
# for i in range((len(word)-1),-1,-1):
#     print(word[i] , end= "")

""" m2 """
# print(word[::-1])


""" Q.6 reverse each word in sentence given by user"""

# sent = input("enter the sentence :- ")
# words = sent.split()
# for word in words:
#     i = len(word) - 1
#     while i >= 0:
#         print(word[i], end = "")
#         i -= 1
#     print(" ", end="")

# 1st we select word by for loop, 
# next we choose letter by index, 
# then we reverse using while, 
# then we print reverse letters and to keep them in same line we use end, 
# and when while loop end we again print space and keep it in same line.....
# so for loop worked for one time -> now it's time to another word

"""m2"""
# sent = input("enter the sentence :- ")
# words = sent.split()
# for letters in words:
#     print(letters[::-1], end= " ")

"""m3"""
# sent = input("enter the sentence :- ")
# words = sent.split()
# result = " ".join([letters[::-1] for letters in words])
# print(result)


""" Q.7 user wants to count vowerls and consonents in word, with index"""
# word = input("enter the word: ").lower()
# vowels = 0
# consonents = 0
# for char in word:
#     if char.isalpha():
#         if char in "aeiou":
#             vowels += 1
#         else:
#             consonents += 1
# print(f"vowels : {vowels} \nconsonents : {consonents}")

""" Q.8 user want to know which consonents and how many times comes in his stings"""
# str = input("enter your words :- ").lower()
# vowel = "aeiou"
# index = 0
# count = {}
# while index < len(str):
#     char = str[index]
#     if char not in vowel and char.isalpha():
#         if char in count:
#             count[char] += 1
#         else:
#             count[char] = 1
#     index += 1
# print(count)

""" Q.9 check given number is perfect or not"""
num = int(input("tell your number :-"))

