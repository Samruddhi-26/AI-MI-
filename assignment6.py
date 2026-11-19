# 1. Write a Python program to reverse a number without converting it into a string.
# num=int(input("enter a number"))
# rev = 0

# while num > 0:
#     rem = num % 10
#     rev = rev * 10 + rem
#     num = num // 10

# print("Reverse number:", rev)

# 2.Write a program to check whether a number is a palindrome.
# num = int(input("Enter a number: "))
# temp = num
# rev = 0

# while num > 0:
#     rem = num % 10
#     rev = rev * 10 + rem
#     num = num // 10

# if temp == rev:
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome Number")

# 3. Write a program to check whether a number is an Armstrong number.
# num = int(input("Enter a number: "))
# temp = num
# total = 0

# while num > 0:
#     rem = num % 10
#     total = total + rem ** 3
#     num = num // 10

# if temp == total:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")

# 4.Write a program to find the factorial of a number using a loop.
# num = int(input("Enter a number: "))
# fact = 1

# for i in range(1, num + 1):
#     fact = fact * i

# print("Factorial:", fact)

# 5.Write a program to generate the Fibonacci series up to N terms.

# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c

# 6.Write a program to check whether a number is prime.
# num = int(input("Enter a number: "))

# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a Prime Number")
#             break
#     else:
#         print("Prime Number")
# else:
#     print("Not a Prime Number")

# 7.Write a program to print all prime numbers between 1 and 100.
# for num in range(2, 101):
#     count = 0

#     for i in range(1, num + 1):
#         if num % i == 0:
#             count = count + 1

#     if count == 2:
#         print(num, end=" ")

# 8.. Write a program to find the GCD and LCM of two numbers.
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# gcd = 1

# for i in range(1, min(a, b) + 1):
#     if a % i == 0 and b % i == 0:
#         gcd = i

# lcm = (a * b) // gcd

# print("GCD:", gcd)
# print("LCM:", lcm)

# 9. Write a program to reverse a string without using slicing.
# str1 = input("Enter a string: ")
# rev = ""

# for i in str1:
#     rev = i + rev

# print("Reverse string:", rev)

# 10.Write a program to check whether a string is a palindrome.
# str1 = input("Enter a string: ")

# rev = ""

# for i in str1:
#     rev = i + rev

# if str1 == rev:
#     print("Palindrome String")
# else:
#     print("Not a Palindrome String")

# 11.Write a program to count vowels, consonants, digits and special characters in a string.
# str1 = input("Enter a string: ")

# vowels = 0
# consonants = 0
# digits = 0
# special = 0

# for i in str1:
#     if i.isalpha():
#         if i.lower() in "aeiou":
#             vowels = vowels + 1
#         else:
#             consonants = consonants + 1

#     elif i.isdigit():
#         digits = digits + 1

#     else:
#         special = special + 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)
# print("Digits:", digits)
# print("Special Characters:", special)   

# 12. Write a program to find the frequency of each character in a string.
# str1 = input("Enter a string: ")

# freq = {}

# for i in str1:
#     if i in freq:
#         freq[i] = freq[i] + 1
#     else:
#         freq[i] = 1

# print("Character Frequency:", freq)

# 13.Write a program to find the first non-repeating character in a string.
# str1 = input("Enter a string: ")

# for i in str1:
#     if str1.count(i) == 1:
#         print("First non-repeating character:", i)
#         break
# else:
#     print("No non-repeating character found")

# 14.Write a program to remove duplicate characters from a string.
# str1 = input("Enter a string: ")
# result = ""

# for i in str1:
#     if i not in result:
#         result = result + i

# print("String after removing duplicates:", result)

# 15.Write a program to check whether two strings are anagrams.
# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")

# if len(str1) == len(str2):
#     if sorted(str1) == sorted(str2):
#         print("Anagram")
#     else:
#         print("Not Anagram")
# else:
#     print("Not Anagram")

# 16. Write a program to find the longest word in a sentence.
# str1 = input("Enter a sentence: ")

# words = str1.split()
# longest = ""

# for i in words:
#     if len(i) > len(longest):
#         longest = i

# print("Longest word:", longest)

# 17.Find the second-largest element in a list without using sort().
# list1 = [10, 20, 40, 30, 50]

# largest = list1[0]
# second = list1[0]

# for i in list1:
#     if i > largest:
#         second = largest
#         largest = i
#     elif i > second and i != largest:
#         second = i

# print("Second largest element:", second)

# 18. Remove duplicate elements from a list without using set().
# list1 = [1, 2, 3, 2, 4, 3, 5]
# result = []

# for i in list1:
#     if i not in result:
#         result.append(i)

# print("List after removing duplicates:", result)

# 19.Find the common elements between two lists
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]

# common = []

# for i in list1:
#     if i in list2:
#         common.append(i)

# print("Common elements:", common)


# 20.Move all zeros to the end of a list without changing the order of other elements.
# list1 = [0, 1, 0, 3, 12]
# result = []

# for i in list1:
#     if i != 0:
#         result.append(i)

# for i in list1:
#     if i == 0:
#         result.append(i)

# print("Updated list:", result)


# 21.Find the missing number in a list containing numbers from 1 to N.
# list1 = [1, 2, 3, 5, 6]
# n = 6

# total = n * (n + 1) // 2
# sum1 = 0

# for i in list1:
#     sum1 = sum1 + i

# missing = total - sum1

# print("Missing number:", missing)

# 22.Find the maximum difference between two elements where the larger element appears after the smaller element.
# list1 = [2, 3, 10, 6, 4, 8]

# min1 = list1[0]
# max_diff = list1[1] - list1[0]

# for i in range(1, len(list1)):
#     diff = list1[i] - min1

#     if diff > max_diff:
#         max_diff = diff

#     if list1[i] < min1:
#         min1 = list1[i]

# print("Maximum difference:", max_diff)

# 23. Rotate a list to the right by K positions.
# list1 = [1, 2, 3, 4, 5]
# k = 2

# for i in range(k):
#     last = list1.pop()
#     list1.insert(0, last)

# print("Rotated list:", list1)

# 24.Find all pairs in a list whose sum equals a given target.
# list1 = [2, 4, 3, 5, 7, 8]
# target = 10

# for i in range(len(list1)):
#     for j in range(i + 1, len(list1)):
#         if list1[i] + list1[j] == target:
#             print(list1[i], list1[j])


# 25. Write a program to count the frequency of each word in a paragraph.
# str1 = input("Enter a paragraph: ")

# words = str1.split()
# freq = {}

# for i in words:
#     if i in freq:
#         freq[i] = freq[i] + 1
#     else:
#         freq[i] = 1

# print("Word Frequency:", freq)


# 26. Write a program to merge two dictionaries. If a key exists in both, add their values.
# dict1 = {'a': 10, 'b': 20, 'c': 30}
# dict2 = {'b': 5, 'c': 10, 'd': 40}

# result = dict1.copy()

# for i in dict2:
#     if i in result:
#         result[i] = result[i] + dict2[i]
#     else:
#         result[i] = dict2[i]

# print("Merged Dictionary:", result)


# 27.Write a program to sort a dictionary based on its values.
# dict1 = {'a': 40, 'b': 10, 'c': 30, 'd': 20}

# result = sorted(dict1, key=dict1.get)

# print("Sorted Dictionary:", result)


# 28.Given a list of student dictionaries containing name and marks, find the student with the highest marks.
# students = [
#     {'name': 'Amit', 'marks': 85},
#     {'name': 'Rahul', 'marks': 90},
#     {'name': 'Priya', 'marks': 95},
#     {'name': 'Sneha', 'marks': 80}
# ]

# highest = students[0]

# for i in students:
#     if i['marks'] > highest['marks']:
#         highest = i

# print("Student Name:", highest['name'])
# print("Highest Marks:", highest['marks'])


# 29.Group words from a list based on their first character using a dictionary.
# words = ['apple', 'ant', 'banana', 'ball', 'cat', 'car']

# result = {}

# for i in words:
#     first = i[0]

#     if first in result:
#         result[first].append(i)
#     else:
#         result[first] = [i]

# print("Grouped Words:", result)


# 30. Convert two lists into a dictionary, where the first list contains keys and the second contains values.
# keys = ['name', 'age', 'city']
# values = ['Samruddhi', 21, 'Pune']

# result = {}

# for i in range(len(keys)):
#     result[keys[i]] = values[i]

# print("Dictionary:", result)


# 31. Write a recursive function to calculate the factorial of a number.
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# num = int(input("Enter a number: "))

# result = factorial(num)

# print("Factorial:", result)


# 32. Write a recursive function to find the sum of digits of a number.
# def sum_digits(n):
#     if n == 0:
#         return 0
#     else:
#         return (n % 10) + sum_digits(n // 10)

# num = int(input("Enter a number: "))

# result = sum_digits(num)

# print("Sum of digits:", result)

# 33.Implement your own map() function without using Python's built-in map().
# def my_map(func, numbers):
#     result = []

#     for num in numbers:
#         result.append(func(num))

#     return result


# def square(n):
#     return n * n


# numbers = [1, 2, 3, 4, 5]

# result = my_map(square, numbers)

# print("Original List:", numbers)
# print("Square List:", result)


# 34. Implement a function that accepts a list and returns a new list containing only even numbers.
# def even_numbers(numbers):
#     result = []

#     for num in numbers:
#         if num % 2 == 0:
#             result.append(num)

#     return result


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# result = even_numbers(numbers)

# print("Even Numbers:", result)


# 35.Write a function to flatten a nested list
# def flatten_list(nested_list):
#     result = []

#     for item in nested_list:
#         if isinstance(item, list):
#             result.extend(flatten_list(item))
#         else:
#             result.append(item)

#     return result


# numbers = [1, [2, 3], [4, [5, 6]], 7]

# result = flatten_list(numbers)

# print("Flattened List:", result)

# 36.Student Management System

# Create a console-based application with the following operations:
# - Add student
# - Display all students
# - Search student by ID
# - Update student details
# - Delete student



# students = []


# # Add Student
# def add_student():
#     sid = int(input("Enter Student ID: "))
#     name = input("Enter Student Name: ")
#     age = int(input("Enter Student Age: "))
#     marks = float(input("Enter Student Marks: "))

#     student = {
#         "id": sid,
#         "name": name,
#         "age": age,
#         "marks": marks
#     }

#     students.append(student)
#     print("Student added successfully!")


# # Display All Students
# def display_students():
#     if len(students) == 0:
#         print("No students found.")
#     else:
#         for student in students:
#             print(student)


# # Search Student
# def search_student():
#     sid = int(input("Enter Student ID to search: "))

#     for student in students:
#         if student["id"] == sid:
#             print("Student Found:", student)
#             return

#     print("Student not found.")


# # Update Student
# def update_student():
#     sid = int(input("Enter Student ID to update: "))

#     for student in students:
#         if student["id"] == sid:
#             student["name"] = input("Enter New Name: ")
#             student["age"] = int(input("Enter New Age: "))
#             student["marks"] = float(input("Enter New Marks: "))

#             print("Student updated successfully!")
#             return

#     print("Student not found.")


# # Delete Student
# def delete_student():
#     sid = int(input("Enter Student ID to delete: "))

#     for student in students:
#         if student["id"] == sid:
#             students.remove(student)
#             print("Student deleted successfully!")
#             return

#     print("Student not found.")


# # Main Menu
# while True:
#     print("\n===== STUDENT MANAGEMENT SYSTEM =====")
#     print("1. Add Student")
#     print("2. Display All Students")
#     print("3. Search Student by ID")
#     print("4. Update Student Details")
#     print("5. Delete Student")
#     print("6. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         add_student()

#     elif choice == 2:
#         display_students()

#     elif choice == 3:
#         search_student()

#     elif choice == 4:
#         update_student()

#     elif choice == 5:
#         delete_student()

#     elif choice == 6:
#         print("Thank you!")
#         break

#     else:
#         print("Invalid choice. Try again.")



# 37. Bank Account Management

# Create a bank account program with:
# - Create account
# - Deposit money
# - Withdraw money
# - Check balance
# - Display account details

# account = {}


# # Create Account
# def create_account():
#     acc_no = int(input("Enter Account Number: "))
#     name = input("Enter Account Holder Name: ")
#     balance = float(input("Enter Initial Balance: "))

#     account["acc_no"] = acc_no
#     account["name"] = name
#     account["balance"] = balance

#     print("Account created successfully!")


# # Deposit Money
# def deposit():
#     amount = float(input("Enter amount to deposit: "))

#     if amount > 0:
#         account["balance"] += amount
#         print("Money deposited successfully!")
#     else:
#         print("Invalid amount!")


# # Withdraw Money
# def withdraw():
#     amount = float(input("Enter amount to withdraw: "))

#     if amount <= 0:
#         print("Invalid amount!")

#     elif amount <= account["balance"]:
#         account["balance"] -= amount
#         print("Money withdrawn successfully!")

#     else:
#         print("Insufficient balance!")


# # Check Balance
# def check_balance():
#     print("Current Balance:", account["balance"])


# # Display Account Details
# def display_details():
#     print("\nAccount Details")
#     print("Account Number:", account["acc_no"])
#     print("Account Holder:", account["name"])
#     print("Balance:", account["balance"])


# # Main Menu
# while True:
#     print("\n===== BANK ACCOUNT MANAGEMENT =====")
#     print("1. Create Account")
#     print("2. Deposit Money")
#     print("3. Withdraw Money")
#     print("4. Check Balance")
#     print("5. Display Account Details")
#     print("6. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         create_account()

#     elif choice == 2:
#         if account:
#             deposit()
#         else:
#             print("Please create an account first!")

#     elif choice == 3:
#         if account:
#             withdraw()
#         else:
#             print("Please create an account first!")

#     elif choice == 4:
#         if account:
#             check_balance()
#         else:
#             print("Please create an account first!")

#     elif choice == 5:
#         if account:
#             display_details()
#         else:
#             print("Please create an account first!")

#     elif choice == 6:
#         print("Thank you for using our bank!")
#         break

#     else:
#         print("Invalid choice!")


# 38. Employee Salary Management

# Create a program to:
# - Add employee details
# - Calculate gross salary
# - Calculate deductions
# - Calculate net salary
# - Display employee salary details

# employee = {}


# # Add Employee Details
# def add_employee():
#     employee["id"] = int(input("Enter Employee ID: "))
#     employee["name"] = input("Enter Employee Name: ")
#     employee["basic"] = float(input("Enter Basic Salary: "))
#     employee["hra"] = float(input("Enter HRA: "))
#     employee["da"] = float(input("Enter DA: "))

#     print("Employee details added successfully!")


# # Calculate Gross Salary
# def gross_salary():
#     gross = employee["basic"] + employee["hra"] + employee["da"]
#     return gross


# # Calculate Deductions
# def deductions():
#     pf = employee["basic"] * 0.12
#     tax = employee["basic"] * 0.05

#     return pf + tax


# # Calculate Net Salary
# def net_salary():
#     net = gross_salary() - deductions()
#     return net


# # Display Salary Details
# def display_details():
#     print("\n===== EMPLOYEE SALARY DETAILS =====")

#     print("Employee ID:", employee["id"])
#     print("Employee Name:", employee["name"])
#     print("Basic Salary:", employee["basic"])
#     print("HRA:", employee["hra"])
#     print("DA:", employee["da"])

#     print("Gross Salary:", gross_salary())
#     print("Deductions:", deductions())
#     print("Net Salary:", net_salary())


# # Main Program
# add_employee()

# display_details()


# 39.Library Management System

# Create a program to:
# - Add books
# - Display available books
# - Issue a book
# - Return a book
# - Search books by title


# books = []


# # Add Book
# def add_book():
#     book_id = int(input("Enter Book ID: "))
#     title = input("Enter Book Title: ")
#     author = input("Enter Author Name: ")

#     book = {
#         "id": book_id,
#         "title": title,
#         "author": author,
#         "status": "Available"
#     }

#     books.append(book)
#     print("Book added successfully!")


# # Display Available Books
# def display_books():
#     print("\nAvailable Books:")

#     found = False

#     for book in books:
#         if book["status"] == "Available":
#             print(book)
#             found = True

#     if not found:
#         print("No available books.")


# # Issue Book
# def issue_book():
#     book_id = int(input("Enter Book ID to issue: "))

#     for book in books:
#         if book["id"] == book_id:
#             if book["status"] == "Available":
#                 book["status"] = "Issued"
#                 print("Book issued successfully!")
#             else:
#                 print("Book is already issued!")
#             return

#     print("Book not found!")


# # Return Book
# def return_book():
#     book_id = int(input("Enter Book ID to return: "))

#     for book in books:
#         if book["id"] == book_id:
#             if book["status"] == "Issued":
#                 book["status"] = "Available"
#                 print("Book returned successfully!")
#             else:
#                 print("This book was not issued!")
#             return

#     print("Book not found!")


# # Search Book by Title
# def search_book():
#     title = input("Enter Book Title to search: ")

#     found = False

#     for book in books:
#         if book["title"].lower() == title.lower():
#             print("Book Found:", book)
#             found = True

#     if not found:
#         print("Book not found!")


# # Main Menu
# while True:
#     print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
#     print("1. Add Book")
#     print("2. Display Available Books")
#     print("3. Issue Book")
#     print("4. Return Book")
#     print("5. Search Book by Title")
#     print("6. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         add_book()

#     elif choice == 2:
#         display_books()

#     elif choice == 3:
#         issue_book()

#     elif choice == 4:
#         return_book()

#     elif choice == 5:
#         search_book()

#     elif choice == 6:
#         print("Thank you for using Library Management System!")
#         break

#     else:
#         print("Invalid choice! Try again.")


# 40.Task Management Application

# Create a console-based task manager with:
# - Add task
# - View all tasks
# - Update task
# - Delete task
# - Mark task as completed
# - Filter completed and pending tasks

# tasks = []


# # Add Task
# def add_task():
#     task_id = int(input("Enter Task ID: "))
#     title = input("Enter Task Title: ")

#     task = {
#         "id": task_id,
#         "title": title,
#         "status": "Pending"
#     }

#     tasks.append(task)
#     print("Task added successfully!")


# # View All Tasks
# def view_tasks():
#     if len(tasks) == 0:
#         print("No tasks available.")
#     else:
#         for task in tasks:
#             print(task)


# # Update Task
# def update_task():
#     task_id = int(input("Enter Task ID to update: "))

#     for task in tasks:
#         if task["id"] == task_id:
#             task["title"] = input("Enter New Task Title: ")
#             print("Task updated successfully!")
#             return

#     print("Task not found!")


# # Delete Task
# def delete_task():
#     task_id = int(input("Enter Task ID to delete: "))

#     for task in tasks:
#         if task["id"] == task_id:
#             tasks.remove(task)
#             print("Task deleted successfully!")
#             return

#     print("Task not found!")


# # Mark Task as Completed
# def complete_task():
#     task_id = int(input("Enter Task ID to complete: "))

#     for task in tasks:
#         if task["id"] == task_id:
#             task["status"] = "Completed"
#             print("Task marked as completed!")
#             return

#     print("Task not found!")


# # Filter Tasks
# def filter_tasks():
#     print("\n1. Completed Tasks")
#     print("2. Pending Tasks")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         status = "Completed"
#     elif choice == 2:
#         status = "Pending"
#     else:
#         print("Invalid choice!")
#         return

#     found = False

#     for task in tasks:
#         if task["status"] == status:
#             print(task)
#             found = True

#     if not found:
#         print("No tasks found!")


# # Main Menu
# while True:
#     print("\n===== TASK MANAGEMENT SYSTEM =====")
#     print("1. Add Task")
#     print("2. View All Tasks")
#     print("3. Update Task")
#     print("4. Delete Task")
#     print("5. Mark Task as Completed")
#     print("6. Filter Tasks")
#     print("7. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         add_task()

#     elif choice == 2:
#         view_tasks()

#     elif choice == 3:
#         update_task()

#     elif choice == 4:
#         delete_task()

#     elif choice == 5:
#         complete_task()

#     elif choice == 6:
#         filter_tasks()

#     elif choice == 7:
#         print("Thank you!")
#         break

#     else:
#         print("Invalid choice! Try again.")