# Given a list of numbers from 1 to n , find the binary value of that number and print the number of maximum successive 1’s present in the binary number

# Example:
# Input: 1111011
# Output: 4




n = int(input())
binar = [int(x) for x in str(n)]
print(binar)
count=0
temp=0
true=0
for i in binar:
    if i==1:
        count+=1
        if temp<count:
            temp=count
    else:
        count=0
print(temp)
