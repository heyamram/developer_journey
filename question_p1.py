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
# print(f"the factorial of ypur no. is {fact}"

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
#     print(f"yor no. (n) is a prime no.")
# else:
#     print(f"yor no. (n) is not a prime no.")

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
    
""" Q.10 user want to seprate digit of their number"""
# n = int(input("tell me your no "))
# while n > 0:
#     print(n % 10)
#     n //= 10

""" Q.9 check user number is pallindrome or not """
n = int(input("tell me your no "))
rev = 0
copy = n
while n > 0:
    rev = (rev * 10) + (n % 10)
    n //= 10      # here we print reverse of our number
if rev == copy:
    print("your no. is pallindromic")
else:
    print("your no. is not pallindromic")


