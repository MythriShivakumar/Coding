#Given a list of numbers from 1 to n , find the second largest number in the list

#Example:
#Input: [4, 3, 2, 9]
#Output: 4




n=int(input(""))
arr=[int(x) for x in input().split()]
unique=[]
for n in arr:
    if n not in unique:
        unique.append(n)
unique.sort()
print(unique[-2])