# 1.Find the data type of every value in a mixed list.
# list=[21,"samu",3.14,True,3+2j,None]
# for value in list:
#     print(value,":",type(value))

# 2.Convert a nested list into a tuple of tuples.
# a=[[1,2,3],[4,5,6],[7,8,9]]
# b=[]

# for i in a:
#     b.append(tuple(i))
#     result=tuple(b)
# print(result)

# 3.Remove all duplicate values from a mixed list while preserving the original order
# list=[1,3,5,"samu",1,5,7,5,8]
# b=[]

# for i in list:
#     if i not in b:
#         b.append(i)
# print(b)

# 4.Check whether a number is a power of 2 using operators.
# num=int(input("enter a number:"))
# if num > 0 and (num &(num-1))==0:
#     print(num,"is power of 2")
# else:
#     print(num,"is not power of 2")

# 5.Swap two numbers using bitwise XOR.
# a=10
# b=20
# a=a^b
# b=a^b
# a=a^b
# print("after swapping a:",a)

# 6.Find whether a number is divisible by both 4 and 6 using logical operators.
# num=int(input("enter a number:"))
# if num % 4 == 0 and num % 6 ==0:
#     print(num,"is divisible by both 4 and 6")
# else:
#     print(num,"is not  divisible by both 4 and 6")

# 7.Calculate the total electricity bill using different unit rates.
# units=int(input("enter the number of units consumbed"))
# if units <= 100:
#     bill = units *5
# elif units <= 200:
#     bill = 100 * 5 + (units -100) * 7
# else:
#     bill = (100 * 5) + (100 * 7) + (units - 200) * 10
# print("total electricity bill is :",bill)    

# 8.Check whether three sides can form a triangle.
# a=int(input("enter the 1st side:"))
# b=int(input("enter the 2nd side:"))
# c=int(input("enter the 3rd side:"))
# if a+b>c and a+c>b and b+c>a:
#     print("the given sides can form a triangle")
# else:
#     print("the given sides cannot form a triangle")

# 9.Determine the type of triangle (Equilateral, Isosceles, Scalene).
# a=int(input("enter the 1st side:"))
# b=int(input("enter the 2nd side:"))
# c=int(input("enter the 3rd side:"))
# if a == b == c:
#     print("the triangle is equilateral")
# elif a == b or b == c or a == c:
#     print("the triangle is isosceles")
# else:
#     print("the triangle is scalene")

# 10. Create a simple ATM menu (Withdraw, Deposit, Balance).
# bal=5000
# print("1.withdraw")
# print("2.deposite")
# print("3.balance")
# ch= int(input("enter your choice:"))
# if ch==1:
#     amt=int(input("enter a amount:"))
#     if amt <=bal:
#         bal=bal-amt
#         print("withdraw money successfully")
#     else:
#         print("unsufficient balance")
# elif ch==2:
#     amt=int(input("enter a amount:"))
#     bal=bal+amt
#     print("deposite money successfully")
# elif ch==3:
#     print("your balance is :",bal)

# 11.Calculate income tax based on different tax slabs
# income=float(input("enter your income:"))
# if income <= 250000:
#     tax=0
# elif income <= 500000:
#     tax = income * 5 / 100

# elif income <= 1000000:
#     tax = income * 10 / 100

# else:
#     tax = income * 20 / 100

# print("Income Tax =", tax)

# 12.Create a menu-driven calculator using if-elif
# print("1.Addition")
# print("2.substraction")
# print("3.multilication")
# print("4.division")
# ch=int(input("enter your choice:"))
# a=int(input("enter a 1st number:"))
# b=int(input("enter a 2nd number:"))
# if ch==1:
#     print("addition is:",a+b)
# elif ch==2:
#     print("substraction is:",a-b)
# elif ch==3:
#     print("multiplication is:",a*b)
# elif ch==4:
#     print("division is :",a/b)   
# else:
#     print("invalid choice")   

# 13.Print all prime numbers between 1 and n
# num=int(input("enter a number:"))
# for n in range(2, num + 1):
#     is_prime = True
#     for i in range(2, n):
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(n, end=" ")

# 14.. Find the factorial of a number using a loop.
# num=int(input("enter a number:"))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
#     print("factorial number is:",fact)

# 15.. Print the Fibonacci series up to n terms.
# num=int(input("enter a number:"))
# a=0
# b=1
# print("fibonacci series:")
# for i in range(num):
#     print(a, end=" ")
#     c=a+b
#     a=b
#     b=c

# 16.Check whether a number is an Armstrong number
# num = int(input("Enter a number: "))

# temp = num
# total = 0

# while temp > 0:
#     digit = temp % 10
#     total = total + digit ** 3
#     temp = temp // 10

# if total == num:
#     print("Armstrong Number")
# else:
#     print("Not Armstrong Number")

# 17.Reverse a number and check if it is a palindrome.
# num=int(input("Enter a number: "))
# temp = num
# reverse = 0
# while temp > 0:
#     digit = temp % 10
#     reverse = reverse * 10 + digit
#     temp = temp // 10
# if num == reverse:
#     print(num, "is a palindrome")
# else:
#     print(num, "is not a palindrome")

# 18.Find the Greatest Common Divisor (GCD) of two numbers
# a=int(input("enter a number:")) 
# b=int(input("enter a number:"))
# while b !=0:
#     temp=b
#     b = a % b
#     a = temp

# print("GCD =", a)

# 19.Write a function to check if a string is a palindrome.

# def is_palinodrome(s):
#      s=s.lower().replace(" ","")
#      return s==s[::-1]

# print(is_palinodrome("a man a plan a canal panama")) 
    
# 20.Write a function to count vowels and consonants in a string
# def count_letters(s):
#     vowels = 0
#     consonants = 0

#     for i in s:
#         if i in "aeiouAEIOU":
#             vowels = vowels + 1
#         elif i.isalpha():
#             consonants = consonants + 1

#     print("Vowels =", vowels)
#     print("Consonants =", consonants)


# name = input("Enter a string: ")
# count_letters(name)

# 21. Create a function to calculate simple and compound interest.
# def simple_interest(p, r, t):
#     si = (p * r * t) / 100
#     print("Simple Interest =", si)


# def compound_interest(p, r, t):
#     ci = p * (1 + r / 100) ** t - p
#     print("Compound Interest =", ci)


# p = int(input("Enter Principal: "))
# r = int(input("Enter Rate: "))
# t = int(input("Enter Time: "))

# simple_interest(p, r, t)
# compound_interest(p, r, t)

# 22. Write a function to return all factors of a number.
# def factors(n):
#     result=[]
#     for i in range(1,n+1):
#         if n %i==0:
#             result.append(i)
#     return result
# print(factors(12))   

#23.  Write a function to find the second-largest number in a list
# def second_lardest(lst):
#     unique_list=list(set(lst))
#     unique_list.sort()
#     if len(unique_list)>=2:
#         return unique_list[-2]
#     else:
#         return None

# print(second_lardest([1,2,3,4,5,6,7,8,9]))

# 24.Merge two lists without duplicates
# def merge_lists(list1,list2):
#     merged_list=list1+list2
#     unique_list=list(set(merged_list))
#     return unique_list

# print(merge_lists([1,2,3,4],[3,4,5,6]))

# 25.Find the second-largest and second-smallest elements
# def sec_lar_small(lst):
#     unique_list=list(set(lst))
#     unique_list.sort()
#     if len(unique_list)>=2:
#         return unique_list[-2],unique_list[1]
#     else:
#         return None,None

# print(sec_lar_small([1,2,3,4,5,6,7,8,9]))    

# 26.. Rotate a list to the left by k positions.
# def rotate_left(lst,k):
#     k=k%len(lst)
#     return lst[k:]+lst[:k]

# print(rotate_left([1,2,3,4,5],2))

# 27.Separate even and odd numbers into two lists
# def separate_even_odd(lst):
#     even_list=[]
#     odd_list=[]
#     for i in lst:
#         if i%2==0:
#             even_list.append(i)
#         else:
#             odd_list.append(i)
#     return even_list,odd_list

# print(separate_even_odd([1,2,3,4,56,7,8,9,10]))

# 28.Find the common elements between two lists.
# a=[1,2,3,4,5,6,7,8,9,10]
# b=[5,6,7,3,8,9,10,11,12]
# common=list(set(a).intersection(set(b)))
# print(common)

# 29.Count the frequency of each element in a tuple
# a = (1, 2, 3, 2, 1, 4, 2, 3)

# for i in a:
#     if a.count(i) > 0:
#         print(i, "=", a.count(i))

# 30.Find the union, intersection, and difference of two sets.
# set1={1,2,3,4,5,6,7}
# set2={5,6,7,8,9,10}
# print("union:",set(set1).union(set(set2)))
# print("interscection:",set(set1).intersection(set(set2)))
# print("diffrence:",set(set1)-set(set2))

# 31.Check whether one set is a subset of another
# a={1,2,3,}
# b={1,2,3,4,5,6}

# if a .issubset(b):
#     print("a is subset of b")
# else:
#     print("a is not subset of b")

# 32.Count the frequency of words in a sentence
# s=input("enter a sentance:")
# words = s.split()
# d={}
# for i in words:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)   

# 33. Create a dictionary from two lists (keys and values).
# keys = ["name", "age", "city"]
# values = ["Samruddhi", 22, "Pune"]

# d = {}

# for i in range(len(keys)):
#     d[keys[i]] = values[i]

# print(d)

# 34.Sort a dictionary by its values
# d = {"name": "samu", "age": 21, "class": "b tech"}

# a = []

# for i in d.values():
#     if type(i) == str:
#         a.append(i)

# print(sorted(a))

# 35.Read a text file and count the number of lines, words, and characters.
# f = open("data.txt", "r")

# data = f.read()

# lines = data.split("\n")
# words = data.split()
# characters = len(data)

# print("Lines:", len(lines))
# print("Words:", len(words))
# print("Characters:", characters)

# f.close()

# 36.Copy only the even-numbered lines from one file to another.
# f1 = open("data.txt", "r")
# f2 = open("new.txt", "w")

# lines = f1.readlines()

# for i in range(len(lines)):
#     if (i + 1) % 2 == 0:
#         f2.write(lines[i])

# print("Even lines copied successfully")

# f1.close()
# f2.close()

# 37.Handle invalid integer input using try-except.
# try:
#     a=int(input("enter a interger number"))
#     print("number=",a)

# except:
#     print("invalid input ")

# 38.Handle file-not-found errors while reading a file
# try:
#     f = open("data.txt", "r")
#     data = f.read()
#     print(data)
#     f.close()

# except FileNotFoundError:
#     print("File not found!")

# 39.Create a random password generator using the random and string modules.
# import random
# import string

# characters = string.ascii_letters + string.digits + string.punctuation

# password = ""

# for i in range(8):
#     password = password + random.choice(characters)

# print("Generated Password:", password)

# 40.Use the datetime module to calculate the number of days between two dates.
from datetime import date

d1 = date(2026, 1, 1)
d2 = date(2026, 1, 10)

result = d2 - d1

print("Number of days =", result.days)






