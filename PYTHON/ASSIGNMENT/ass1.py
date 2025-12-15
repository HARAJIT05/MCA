# 1. Assign values to variables
a = 10
b = 5

print(f"Initial values: a = {a}, b = {b}\n")

# ---------------------------------------------------------
# Requirement 1: Add, subtract, multiply, divide a and b
# ---------------------------------------------------------
print("--- Basic Arithmetic ---")
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b

print(f"Addition (a + b): {addition}")
print(f"Subtraction (a - b): {subtraction}")
print(f"Multiplication (a * b): {multiplication}")
print(f"Division (a / b): {division}")
print()

# ---------------------------------------------------------
# Requirement 2: Show use of arithmetic, logical, and comparison operators
# ---------------------------------------------------------
print("--- Comparison Operators ---")
# Comparing a and b
print(f"Is a greater than b? (a > b): {a > b}")
print(f"Is a equal to b? (a == b): {a == b}")
print(f"Is a not equal to b? (a != b): {a != b}")
print()

print("--- Logical Operators (and, or, not) ---")
# Using boolean logic with the variables
# Example: Check if a is positive AND b is positive
condition_and = (a > 0) and (b > 0)
print(f"(a > 0) and (b > 0): {condition_and}")

# Example: Check if a is 10 OR b is 10
condition_or = (a == 10) or (b == 10)
print(f"(a == 10) or (b == 10): {condition_or}")

# Example: NOT operator reverses the result
condition_not = not (a == b)
print(f"not (a == b): {condition_not}")
print()

# ---------------------------------------------------------
# Requirement 3: Demonstrate operator precedence
# ---------------------------------------------------------
print("--- Operator Precedence ---")
# Expression: a + b * 2 - (a / b)
# Steps breakdown:
# 1. Parentheses first: (a / b) -> (10 / 5) = 2.0
# 2. Multiplication next: b * 2 -> 5 * 2 = 10
# 3. Addition and Subtraction (left to right):
#    a + 10 - 2.0 -> 10 + 10 - 2.0 -> 20 - 2.0 = 18.0

expression_result = a + b * 2 - (a / b)

print(f"Expression: a + b * 2 - (a / b)")
print(f"Result: {expression_result}")

# ---------------------------------------------------------
# Requirement 4 (Question 3): Accept user input and print greeting
# ---------------------------------------------------------
print("\n--- User Input Exercise ---")
name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"Hello, {name}! You are {age} years old.")

# ---------------------------------------------------------
# Requirement 5 (Question 4): Arithmetic with User Input
# ---------------------------------------------------------
print("\n--- Calculator Exercise ---")
print("Please enter two numbers for calculation.")

# Show the use of input()
str_num1 = input("Enter first integer: ")
str_num2 = input("Enter second integer: ")

# Show the use of int() to convert string to integer
num1 = int(str_num1)
num2 = int(str_num2)

# Perform arithmetic operations
calc_sum = num1 + num2
calc_diff = num1 - num2
calc_prod = num1 * num2
calc_div = num1 / num2

# Show the use of print() and string formatting (f-strings)
print(f"You entered {num1} and {num2}.")
print(f"Sum:        {num1} + {num2} = {calc_sum}")
print(f"Difference: {num1} - {num2} = {calc_diff}")
print(f"Product:    {num1} * {num2} = {calc_prod}")
print(f"Division:   {num1} / {num2} = {calc_div}")

# ---------------------------------------------------------
# Requirement 6: LHS vs RHS in Assignment
# ---------------------------------------------------------
print("\n--- LHS vs RHS Demonstration ---")
# LHS (Left-Hand Side) is the destination (variable).
# RHS (Right-Hand Side) is the source (value or expression).

# 1. Simple assignment: x = 5
x = 5
print(f"1. Initial assignment (x = 5): x is {x}")
print("   Explanation: The value 5 (RHS) is assigned to the variable x (LHS).")

# 2. Self-assignment: x = x + 2
# Here, Python evaluates the RHS first using the *current* value of x.
x = x + 2
print(f"2. After update (x = x + 2): x is {x}")
print("   Explanation: RHS (5 + 2) is evaluated to 7, then stored back in LHS (x).")

# 3. Assignment using another variable: y = x * 3
y = x * 3
print(f"3. New variable assignment (y = x * 3): y is {y}")
print(f"   Explanation: RHS (7 * 3) is evaluated to 21, then stored in LHS (y).")