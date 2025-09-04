n=int(input("Enter the number of terms: "))
x=int(input("Enter the value of x: "))
print("series is:")
term=1
print(term, end=" ")
for i in range(1, n):
    term = i * x
    print(term, end=" ")