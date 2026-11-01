#1Write a function is_even(n) that returns "Even" if the number is even, otherwise "Odd".
# def is_even(n):
#     if n%2==0:
#         return "Even"

#     else:
#         return "Odd"

# print(is_even(12))

# print(is_even(7))

# 2Write a function largest(a, b) that returns the larger number
# def largest(a,b):
#     if a>b:
#         return a
#     else:
#         return b

# print(largest(10,20))    
    
# 3.Write a function print_numbers(n) that prints numbers from 1 to n using a loop.
# def print_number(n):
#     for i in range(1,n+1):
#         print(i)
# print_number(15)        

# 4.Write a function sum_n(n) that returns the sum of numbers from 1 to n.
# def sum(n):
#     total=0
#     for i in range(1,n+1):
#         total=total+i
#     return total
# print(sum(10))
    
#5.Write a function table(n) that prints the multiplication table of n from 1 to 10
# def table(n):
#     for i in range(1,11):
#         print(f"{n} * {i} = {n*i}")

# table(10)        

#6.Write a function that takes a list and returns how many even numbers it contains.
# Example:
# count_even([1, 2, 3, 4, 6])
# Output:3

# def count_even(lst):
#     count=0
#     for i in range(len(lst)):
#         if lst[i] % 2==0:
#             count=count+1
#     return count
# print(count_even([1,2,3,4,6]))


#7.Without using max(), write a function that returns the largest number in a list.
 
# def largest_in_list(lst):
#     largest = lst[0]
#     for num in lst:
#         if num > largest:
#             largest = num
#     return largest
# print(largest_in_list([1,2,3,4,6,10,5]))


#8.Write a function that prints numbers from 1 to 100.
# If divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz".
# If divisible by both, print "FizzBuzz".

# def fizzbuzz():
#     for i in range(1, 101):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)

# fizzbuzz()                  


# 9.Write a function that returns True if a string is a palindrome.
# def palindrome(s):
#     if s == s[::-1]:
#         return True
#     else:
#         return False

# print(palindrome("level"))

# 10.Write a function that counts the vowels in a string.
from random import random


def count_vowels(s):
    count = 0

    for ch in s:
        if ch.lower() in "aeiou":
            count += 1

    return count

print(count_vowels("Hello World"))


# 11.Write a function that returns the second largest number in a list without using sort().
def second_largest(lst):
    largest = second = float('-inf')

    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return second

numbers = [10, 25, 5, 40, 30]

print(second_largest(numbers))

# # 12.Generate a random number between 1 and 10.
# Keep asking the user to guess until they get it right.
# Use a loop, conditionals, and functions

import random

def guessing_game():
    num = random.randint(1, 10)

    while True:
        guess = int(input("Guess a number between 1 and 10: "))

        if guess == num:
            print("Correct! You guessed it.")
            break
        else:
            print("Wrong guess! Try again.")


guessing_game()
# 13.Returns "A" for marks ≥ 90
# Returns "B" for marks ≥ 80
# Returns "C" for marks ≥ 70
# Returns "D" for marks ≥ 60
# Otherwise returns "F"


def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

print(grade(95))
print(grade(85))
print(grade(75))
print(grade(65))
print(grade(40))
