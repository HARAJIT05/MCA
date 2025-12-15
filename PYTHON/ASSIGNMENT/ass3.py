import time

# 1. Print the first N natural numbers using a for loop
print("--- 1. Natural Numbers ---")
N = int(input("Enter the value of N: "))
print("First", N, "natural numbers:")
for i in range(1, N + 1):
    print(i, end=" ")
# print() 


# 2. Calculate the factorial of a number using a while loop
print("--- 2. Factorial (While Loop) ---")
num = int(input("Enter a number: "))
factorial = 1
temp_num = num

while temp_num > 0:
    factorial = factorial * temp_num
    temp_num = temp_num - 1

print("The factorial of", num, "is", factorial)
print()

# 3. Demonstrate break, continue, and pass
print("--- 3. Break, Continue, Pass ---")

print("(A) Break Example (Exit loop when i is 5):")
for i in range(1, 11):
    if i == 5:
        print("Loop broken at 5")
        break
    print(i, end=" ")
print()

print("(B) Continue Example (Skip printing 3):")
for i in range(1, 6):
    if i == 3:
        print("(Skipped 3)", end=" ")
        continue
    print(i, end=" ")
print()

print("(C) Pass Example (Placeholder at i=2):")
for i in range(1, 4):
    if i == 2:
        pass 
        print("(Passed at 2)", end=" ")
    else:
        print(i, end=" ")
print()
print()

# 4. Program to print patterns using nested loops
print("--- 4. Triangle Pattern ---")
rows = 4 
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
print()

# 5. Reverse triangle
print("--- 5. Reverse Triangle ---")
rows = 4
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
print()

# 6. Print numbers in steps of 5 between 0 and 50 using range()
print("--- 6. Steps of 5 (0-50) ---")
for i in range(0, 51, 5):
    print(i, end=" ")
print()
print()

# 7. Use range() to create countdown from 10 to 1
print("--- 7. Countdown (10-1) ---")
for i in range(10, 0, -1):
    print(i, end=" ")
    time.sleep(0.1) 
print()
print("Blastoff!")