# Given a list of numbers, where every number shows up twice except for one number, find that one number.

# Example:
# Input: [4, 3, 2, 4, 1, 3, 2]
# Output: 1




n=int(input(""))
arr=[int(x) for x in input().split()]
unique=[]
for n in arr:
    if n not in unique:
        unique.append(n)
diff=(2*sum(unique))-sum(arr)
print(diff)