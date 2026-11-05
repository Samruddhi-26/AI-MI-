#     1.Write a Python program to check whether a number is even or odd.
# num=int(input("enter a number:"))

# if num%2==0:
#     print("given number is even")
# else:
#     print("given number is odd")

# 2.Write a program to find the largest of three numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))

# if a > b and a > c:
#     print("Largest number =", a)

# elif b > a and b > c:
#     print("Largest number =", b)

# else:
#     print("Largest number =", c)


# 3.Write a program to check whether a given number is prime
# num = int(input("Enter a number: "))

# count = 0

# for i in range(1, num + 1):
#     if num % i == 0:
#         count = count + 1

# if count == 2:
#     print("Prime Number")
# else:
#     print("Not Prime Number")


#4.Write a program to print the Fibonacci series up to n terms.
# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c 

# # 5.Write a program to find the factorial of a number using a loop.
# num = int(input("Enter a number: "))

# fact = 1

# for i in range(1, num + 1):
#     fact = fact * i

# print("Factorial =", fact)

# 6.Write a program to reverse a string without using [::-1].
# s = input("Enter a string: ")

# rev = ""

# for i in s:
#     rev = i + rev

# print("Reverse string =", rev)

# 7.Write a program to check whether a string is a palindrome.
# s = input("Enter a string: ")

# rev = ""

# for i in s:
#     rev = i + rev

# if s == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# 8.Write a program to count the number of vowels and consonants in a string.
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

# 9.Write a program to find the sum of all elements in a list
# list=[23,14,52,24]
# sum=0
# for i in list:
#     sum=sum+i
# print(sum)  

# 10.Write a program to find the largest and smallest element in a list without using max()
# or min(). 

# a = [12, 31, 55, 21, 1, 23, 41]

# a.sort()

# print("Smallest element:", a[0])
# print("Largest element:", a[-1])


# 11.Write a program to remove duplicate elements from a list

# list=[1,1,2,3,4,5,6,4,5,3]

# unique=set(list)
# print(unique)

# 12.Write a program to count how many times each element appears in a list using a
# dictionary.

# a = [1, 2, 3, 2, 1, 4, 2, 3]

# d = {}

# for i in a:
#     if i in d:
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1

# print(d)

# 13.Write a program to find the second-largest number in a list
# list=[1,2,3,4,5,7,8]
# list.sort()
# print(list[-2])

# 14.Write a program to sort a list without using sort() or sorted().
# a = [5, 2, 8, 1, 3]

# for i in range(len(a)):
#     for j in range(len(a)-1):
#         if a[j] > a[j+1]:
#             temp = a[j]
#             a[j] = a[j+1]
#             a[j+1] = temp

# print("Sorted list:", a)

# 15.Write a function that accepts a list of numbers and returns a list containing only the even
# numbers
# def even_num(a):
#     even = []

#     for i in a:
#         if i % 2 == 0:
#             even.append(i)

#     return even


# print(even_num([1, 2, 3, 4, 5, 6, 7]))   


# 16.Write a program to find the frequency of each character in a string.
# s = input("Enter a string: ")

# d = {}

# for i in s:
#     if i in d:
#         d[i] = d[i] + 1
#     else:
#         d[i] = 1

# print(d)

# 17. Write a program to check whether two strings are anagrams of each other.
# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")

# if sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not Anagram")

# 18.Write a program to find all duplicate values in a list.
# a = [1, 2, 3, 2, 4, 5, 1, 3]

# duplicate = []

# for i in a:
#     if a.count(i) > 1 and i not in duplicate:
#         duplicate.append(i)

# print("Duplicate values:", duplicate)

# 19.Write a program that takes a sentence and finds the longest word.
# s = input("Enter a sentence: ")

# words = s.split()
# longest = ""

# for i in words:
#     if len(i) > len(longest):
#         longest = i

# print("Longest word:", longest)

# 20. Create a simple student marks program that:
# a. accepts marks for 5 subjects,
# b. calculates the total and percentage,
# c. assigns a grade,and displays whether the student passed or failed.
        
total = 0

for i in range(1, 6):
    marks = int(input("Enter marks: "))
    total = total + marks

percentage = total / 5

print("Total Marks:", total)
print("Percentage:", percentage, "%")

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 35:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

if percentage >= 35:
    print("Result: Pass")
else:
    print("Result: Fail")