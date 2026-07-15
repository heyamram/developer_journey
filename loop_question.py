#      while loop question

""" Q.1 print number from 10 to 15"""
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
str = input("enter your words :- ").lower()
vowel = "aeiou"
index = 0
count = {}
while index < len(str):
    char = str[index]
    if char not in vowel and char.isalpha():
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    index += 1
print(count)