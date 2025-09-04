a=int(input("Enter the first term (a): "))
d=int(input("Enter the common difference (d): "))
n=int(input("Enter the number of terms (n): "))
print("Arithmetic Progression:", end=" ")
for i in range(n):
    print(a + i * d, end=" ")