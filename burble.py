
import sys

n = int(input().strip())
a = map(int, input().strip().split(' '))
# Write Your Code Here
totalswaps = 0
for i in range(n -1 , 0):
    numberofswaps  = 0
    for j in range(0, i):
        if(a[j] > a[j + 1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            numberofswaps = numberofswaps + 1
            totalswaps += 1
    if (numberofswaps == 0):
        break
    
print("Array is sorted in "+str(totalswaps)+" swaps.")
print("First Element: "+str(a[0]))
print("Last Element: "+str(a[n-1]))  
