# Python Data Structures Assignment Solution
# This script covers Lists, Tuples, and Sets as requested.

print("--- TASK 1: CREATE LIST ---")
# 1. Create a list of integers from 1 to 10.
numbers = list(range(1, 11))
print(f"Original list: {numbers}")
print()

print("--- TASK 2: LIST OPERATIONS ---")
# 2. Perform various list operations:

# append() and insert()
numbers.append(11)          # Adds 11 to the end
numbers.insert(0, 0)        # Inserts 0 at index 0
print(f"After append(11) and insert(0, 0): {numbers}")

# Update specific element using index
numbers[5] = 99             # Updates the element at index 5 to 99
print(f"After updating index 5 to 99: {numbers}")

# Delete specific elements using index and value
del numbers[5]              # Deletes the element at index 5 (which was 99)
print(f"After deleting index 5: {numbers}")
# Sort and reverse the list
numbers.sort()              # Sorts in ascending order
print(f"Sorted list: {numbers}")

numbers.reverse()           # Reverses the list in place
print(f"Reversed list: {numbers}")

# Slice the list
first_five = numbers[:5]
every_second = numbers[::2]
print(f"First 5 elements: {first_five}")
print(f"Every second element: {every_second}")

# List comprehension: squares of even numbers
# We'll use a new range 1-10 for clarity
even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
print(f"Squares of even numbers (1-10): {even_squares}")
print()

print("--- TASK 3: CREATE TUPLES ---")
# 3. Create tuples with:
mixed_tuple = (1, "Python", 3.14)
single_element_tuple = (5,)  # Note the comma is essential
nested_tuple = (1, (2, 3), 4)

print(f"Mixed tuple: {mixed_tuple}")
print(f"Single element tuple: {single_element_tuple}")
print(f"Nested tuple: {nested_tuple}")
print()

print("--- TASK 4: TUPLE OPERATIONS ---")
# 4. Demonstrate tuple features:

# Tuple unpacking
a, b, c = mixed_tuple
print(f"Unpacked mixed_tuple: a={a}, b={b}, c={c}")

# Access by indexing
print(f"Element at index 1 of mixed_tuple: {mixed_tuple[1]}")
print(f"Accessing nested element (2) in nested_tuple: {nested_tuple[1][0]}")

# Methods like count() and index()
sample_tuple = (1, 2, 3, 2, 4, 2)
count_of_twos = sample_tuple.count(2)
index_of_four = sample_tuple.index(4)

print(f"In tuple {sample_tuple}:")
print(f"  - The number 2 appears {count_of_twos} times.")
print(f"  - The number 4 is at index {index_of_four}.")
print()

print("--- TASK 5: CREATE SET ---")
# 5. Create a set from a list with duplicates
list_with_duplicates = [1, 2, 2, 3, 4, 4, 4, 5]
unique_set = set(list_with_duplicates)
print(f"List with duplicates: {list_with_duplicates}")
print(f"Set (duplicates removed): {unique_set}")
print()

print("--- TASK 6: SET OPERATIONS ---")
# 6. Apply set methods:

# add() and remove()
unique_set.add(6)
print(f"After adding 6: {unique_set}")

unique_set.remove(1)
print(f"After removing 1: {unique_set}")

# Set operations with another set
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Union (all elements from both)
print(f"Union (A | B): {set_a.union(set_b)}")

# Intersection (common elements)
print(f"Intersection (A & B): {set_a.intersection(set_b)}")

# Difference (elements in A but not in B)
print(f"Difference (A - B): {set_a.difference(set_b)}")
print()

print("--- TASK 7: SET COMPREHENSION ---")
# 7. Use set comprehension to find squares of numbers divisible by 3
# We'll check numbers from 1 to 20
squares_div_by_3 = {x**2 for x in range(1, 21) if x % 3 == 0}
print(f"Squares of numbers divisible by 3 (from range 1-20): {squares_div_by_3}")