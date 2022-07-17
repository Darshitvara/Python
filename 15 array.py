
from array import *

arr = array('i',[])   #Empty Array declaration

flag=1

while flag==1:      # For infinit loop iteration
     print("Enter Value : ",end='')
     val = int(input())
     arr.append(val)
     print("Do You Want To Add More Integer Elements In Array ? Y/y ")
     yn = input()
     if yn != 'y' and yn != 'Y': #Condition for exit loop
          flag = 0

print("\n")   
i=0
j=1
for i in range(len(arr)):    #sorting array
     for j in range(len(arr)):
          if arr[i] < arr[j] :
               temp = arr[j]
               arr[j] = arr[i]
               arr[i] = temp

print("Enter value you want to search : ",end='')   # To search array element
v = int(input())
print("\n") 
i=0
for i in range(len(arr)):
     if arr[i] == v:
          print("Value ",v," is on array index ",end='')
          print(i+1)
          break
print("\n")   

print(arr.buffer_info()) # Array address and length