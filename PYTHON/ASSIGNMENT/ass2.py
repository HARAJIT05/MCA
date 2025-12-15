# 1. Program to check whether a number is even or odd.
print("--- 1. Check Even or Odd ---")
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is Even")
else:
    print(f"{number} is Odd")


# 2. Program to determine whether a number is positive, negative, or zero.
print("\n--- 2. Positive, Negative, or Zero ---")
number = float(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# 3. Program to find the greatest among three numbers.
print("\n--- 3. Greatest of Three Numbers ---")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    greatest = num1
elif num2 >= num1 and num2 >= num3:
    greatest = num2
else:
    greatest = num3
    
print(f"The greatest number is: {greatest}")


# 4. Check whether a year entered by the user is a leap year.
print("\n--- 4. Check Leap Year ---")
year = int(input("Enter a year: "))
# A year is a leap year if it is divisible by 4,
# except for end-of-century years, which must be divisible by 400.
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# 5. Student grade calculator.
print("\n--- 5. Student Grade Calculator ---")
percentage = float(input("Enter percentage: "))

if percentage > 85:
    grade = "A grade"
elif 75 <= percentage <= 85:
    grade = "B grade"
elif 50 <= percentage < 75:
    grade = "C grade"
elif 30 <= percentage < 50:
    grade = "D grade"
else:
    grade = "Fail"
    
print(f"Result: {grade}")