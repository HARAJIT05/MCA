import math
a=float(input("Enter length of first side: "))
b=float(input("Enter length of second side: "))
c=float(input("Enter length of third side: "))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of triangle is:",area)