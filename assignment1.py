# 1.Check if a number is positive, negative, or zero

# a=int(input("enter a number:"))

# if a>0:
#     print("given number is positive")

# elif a<0:
#     print("given number is negative")

# else:
#     print("given number is zero")


# 2.Check whether a number is even or odd.

# a= int(input("enter a number"))

# if a % 2==0:
#     print("given number even")

# else:
#     print("given number is odd")


#3.Find the greater of two numbers.

# num1= int(input("enter a number1:"))
# num2= int(input("enter a number2:"))

# if num1 > num2:
#     print(num1,"this is greater number")

# else:
#     print(num2,"this is greater number")   


#4. Find the greatest of three numbers.

# a= int(input("enter a number 1:"))
# b= int(input("enter a number 2:"))
# c= int(input("enter a number 3:"))

# if a>b:
#     print(a," is greater number ")

# elif b>a:
#     print(b,"is greater number")    

# else:
#     print(c,"is grater number")    

#5.Check if a person is eligible to vote (age ≥ 18)

# age= int(input("enter a age of person:"))

# if age >=18:
#     print("person is eligible for vote")

# else:
#     print("person is not eligible for vote")    

#6.Check whether a year is a leap year.
# year=int(input("enter a year:"))
# if year % 4==0:
#     print("leap year")
# elif year % 100 == 0   :
#     print("not a leap year") 
# elif year % 4==0:

#     print(" leap year")  
# else:
#     print("not a leap year")      

#7.Check if a character is a vowel or consonant
# ch = input("enter a character:")

# if ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U":
#     print("it is vowels")

# else:
#     print("it is consonant")    

#8.Check whether a number is divisible by 5 and 11.

# a= int(input("enter a number:"))

# if a % 5==0:
#     print("number is divisible by 5")
# elif a % 11==0:
#     print("number is divisible by 11")
# else:
#     print("number is not divisible by both")        

#9.Check if a number is a multiple of both 3 and 7.
# a= int(input("enter a number:"))

# if a % 3==0 and a % 7==0:
#     print("number is multiple by both") 

# else:
#     print("number is not multiple by both")    

#10.Assign grades based on marks  a. 90–100: A
# b. 80–89: B
# c. 70–79: C
# d. 60–69: D
# e. Below 60: F

# marks= int(input("enter your marks:"))

# if marks >=90 and marks < 100:
#     print("your grade is A")

# elif marks >= 80 and marks <  90   :
#     print("your grade is B")

# elif marks >=70 and marks < 80: 
#     print("your grade is C")

# elif marks >=60 and marks < 70 :
#     print("your grade is D")

# elif marks < 60:
#     print("you are fail") 
# else :
#     print("invalid marks")         


#11.Check if a character is uppercase or lowercase

# ch= input("enter a character:")

# if ch .isupper():
#     print("character is uppercase")
# elif ch.islower():
#     print("character is lowercase")
# else:
#     print("invalid character")        


#12.Find whether the entered alphabet is a vowel using if-elif.

# ch= input("enter a character:").lower()

# if ch=="a":
#     print("it is vowel")
# elif ch=="e":
#     print("it is vowel")
        
# elif ch=="i":
#     print("it is vowel")

# elif ch=="o":
#     print("it is vowel")

# elif ch=="u":
#     print("it is vowel")

# else:
#     print("it is consonant")

#13. Check if three sides can form a triangle

# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if a + b > c and a + c > b and b + c > a:
#     print("Triangle can be formed")
# else:
#     print("Triangle cannot be formed")

#14.Determine the type of triangle (Equilateral, Isosceles, Scalene).

# a = int(input("Enter first side: "))
# b = int(input("Enter second side: "))
# c = int(input("Enter third side: "))

# if a <= 0 or b <= 0 or c <= 0:
#     print("Invalid sides")
# elif a + b <= c or a + c <= b or b + c <= a:
#     print("Triangle cannot be formed")
# elif a == b and b == c:
#     print("Equilateral Triangle")
# elif a == b or b == c or a == c:
#     print("Isosceles Triangle")
# else:
#     print("Scalene Triangle")

#15.Find the largest among four numbers.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# d = int(input("Enter fourth number: "))

# if a >= b and a >= c and a >= d:
#     print("Largest number is:", a)
# elif b >= a and b >= c and b >= d:
#     print("Largest number is:", b)
# elif c >= a and c >= b and c >= d:
#     print("Largest number is:", c)
# else:
#     print("Largest number is:", d)


#16.Check whether a number is a three-digit number.

# num = int(input("Enter a number: "))

# if 100 <= abs(num) <= 999:
#     print("Three-digit number")
# else:
#     print("Not a three-digit number")


#17. Calculate electricity bill using slab rates

# unit= int(input("enter a bill unit:"))

# if unit <=0:
#     print("invalid unit")
# elif unit <= 100:
#     bill=unit*5
#     print("electricity bill",bill)    
# elif unit <= 200:
#     bill = 100 * 5 + (unit - 100) * 7
#     print("Electricity bill:", bill)
# else:
#     bill = 100 * 5 + 100 * 7 + (unit - 200) * 10
#     print("Electricity bill:", bill)
    
#18.Calculate income tax based on income slabs

# income = float(input("Enter your  income: "))

# if income <= 250000:
#     tax = 0
# elif income <= 500000:
#     tax = income * 0.05
# elif income <= 1000000:
#     tax = income * 0.20
# else:
#     tax = income * 0.30

# print("Income tax:", tax)


#19 . Check if a student passes (minimum 35 marks in each subject)
# maths= int(input("enter your maths marks:"))
# science= int(input("enter your science marks:"))
# english= int(input("enter your english marks: "))

# if maths >35 and science >35 and english >35:
#     print("you are pass")
# else:
#     print("you are fail")    

#20.Find whether a number is within a given range.

# num = int(input("Enter a number: "))
# start = int(input("Enter range start: "))
# end = int(input("Enter range end: "))

# if num >= start and num <= end:
#     print("Number is within the range")
# else:
#     print("Number is outside the range")

#21.Build a simple calculator using if-elif-else (+, -, *, /)

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /): ")

# if op == "+":
#     print("Result:", num1 + num2)
# elif op == "-":
#     print("Result:", num1 - num2)
# elif op == "*":
#     print("Result:", num1 * num2)
# elif op == "/":
#     if num2 != 0:
#         print("Result:", num1 / num2)
#     else:
#         print("Cannot divide by zero")
# else:
#     print("Invalid operator")


#22.Check if a year is a century leap year.

# year = int(input("Enter a year: "))

# if year % 100 == 0 and year % 400 == 0:
#     print("Century Leap Year")
# elif year % 100 == 0:
#     print("Not a Leap Year")
# else:
#     print("Not a Century Year")

#23.Determine the season based on the month number

# month = int(input("Enter month number (1-12): "))

# if month in (3, 4, 5):
#     print("Summer Season")
# elif month in (6, 7, 8, 9):
#     print("Rainy Season")
# elif month in (10, 11):
#     print("Autumn Season")
# elif month in (12, 1, 2):
#     print("Winter Season")
# else:
#     print("Invalid month number")


#24.Check whether a password meets minimum conditions (length, digits, etc.).

# password = input("Enter password: ")

# if len(password) >= 8 and any(ch.isdigit() for ch in password):
#     print("Valid Password")
# else:
#     print("Invalid Password")

#25.Determine ticket price based on age category.
    
# age = int(input("enter your age:"))
# if age <6:
#     print("Ticket is free")
# elif age <=12 :
#     print("Ticket is price is .50")
# elif age <=59:
#     print("Ticket is price is .100")   
# elif age <=70:
#     print("Ticket is price is.70")         


#26.Calculate discount based on purchase amount.

# amount = float(input("Enter purchase amount: "))

# if amount >= 5000:
#     discount = amount * 0.20
# elif amount >= 3000:
#     discount = amount * 0.10
# elif amount >= 1000:
#     discount = amount * 0.05
# else:
#     discount = 0

# print("Discount:", discount)
# print("Final amount:", amount - discount)


#27.Check if a person is eligible for a driving license (age and eyesight condition).

# age = int(input("Enter your age: "))
# eyesight = input("Is your eyesight normal? (yes/no): ").lower()

# if age >= 18 and eyesight == "yes":
#     print("Eligible for driving license")
# else:
#     print("Not eligible for driving license")


#28.Create a login system with username and password validation.

# username = input("Enter username: ")
# password = input("Enter password: ")

# if username == "samruddhi" and password == "12345":
#     print("Login successful")
# else:
#     print("Invalid username or password")

#29 Find the number of days in a month

# month = int(input("Enter month number (1-12): "))

# if month == 2:
#     print("28 or 29 days")
# elif month in (4, 6, 9, 11):
#     print("30 days")
# elif 1 <= month <= 12:
#     print("31 days")
# else:
#     print("Invalid month")

#30.Create a menu-driven program using if-elif-else with options like:
# a. Addition
# b. Subtraction
# c. Multiplication
# d. Division
# e. Exit



print("a. Addition")
print("b. Subtraction")
print("c. Multiplication")
print("d. Division")
print("e. Exit")

ch = input("Enter your choice: ")

if ch == 'a':
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a + b)

elif ch == 'b':
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a - b)

elif ch == 'c':
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a * b)

elif ch == 'd':
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")

elif ch == 'e':
    print("Exit")

else:
    print("Invalid choice")
