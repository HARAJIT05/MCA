import numpy as np
import pandas as pd

print("Printing The Array")

arr=np.array([2,3,4])
print(arr)

print("Printing The 2D Array")

arr1=np.array([(700,210,120),(400,90,30)])
print(arr1)

print("Sorting The Array")
arr4=np.sort(arr1,axis=1)
print(arr4)

print("Appending The Array")
arr5=np.append(arr4,10)
print(arr5)

print("Inserting The Array")
arr6=np.insert(arr5,3,70)
print(arr6)

print("Deleting column 1 from The Array")
arr7=np.delete(arr1,1,axis=1)
print(arr7)

print("Deleting Row from The Array")
arr8=np.delete(arr1,0,axis=0)
print(arr8)

print("Creating New Array")
new_arr=np.array([(400,300,110),(110,90,30)])
print(new_arr)


print("Concatenating The Array in Axis 0 (Rows)")
arr9=np.concatenate((arr1,new_arr),axis=0)
print(arr9)

print("Concatenating The Array in Axis 1 (Columns)")
arr10=np.concatenate((arr1,new_arr),axis=1)
print(arr10)

print("Splitting The Array in 2 parts")
arr11=np.split(arr1,2)
print(arr11)

print("Dividing The Array Elements into half")
arr12=np.divide(arr1,2)
print(arr12)

print("To the power of 3 for each element in The Array")
arr13=np.power(arr1,3)
print(arr13)

print("Creating New Array 3")
arrnewnew=np.array([(30,40,50),(20,10,20)])
print(arrnewnew)

print("Creating another Array 4")
arr2=np.array([(20,30,10),(30,90,30)])
print(arr2)

print("Adding Two Arrays")
arr14=np.add(arrnewnew,arr2)
print(arr14)

print("Square Root of The Array Elements")
arr15=np.sqrt(arrnewnew)
print(arr15)

print("Angle of the elements in The Array")
arr16=np.cos(arrnewnew)
print(arr16)

print("Printing The log of The Array Elements")
arr17=np.log(arrnewnew)
print(arr17)