
# my_tuple = (1, 2, 3, 4, 5)

# my_list = list(my_tuple)

# print("Tuple:", my_tuple)
# print("List:", my_list)

# my_list2 = [10, 20, 30, 40, 50]
# my_tuple2 = tuple(my_list2)
# print("List:2", my_list2)
# print("Tuple:2", my_tuple2)

# set1 = {1, 2, 3, 4, 5}
# my_tuple3 = tuple(set1)
# print("Set:", set1)
# print("Tuple:3", my_tuple3)

# my_tuple4 = ('a', 'b', 'c', 'd')
# set2 = set(my_tuple4)
# print("Tuple:4", my_tuple4)
# print("Set:2", set2)


# set3 = {10, 20, 30, 40}
# my_tuple5 = tuple(set3)
# print("Set:3", set3)
# print("Tuple:5", my_tuple5)

##Transpose of Matrix
matrix = [[1, 2, 3], 
          [4, 5, 6],
          [7, 8, 9]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Original Matrix:")
for row in matrix:
    print(row)
print("Transposed Matrix:")
for row in transpose:
    print(row)
