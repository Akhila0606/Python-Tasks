# 1.	Check if year is a leap year
# Input: Year (integer)
# Output: Leap year or Not a leap year
n=int(input("Enter a year:"))
if n%4==0 and (n%100!=0 or n%400==0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Output:-
# Enter a year:2000
# Leap Year

# 2.	 Write a Python program to check whether the given list is sorted in ascending order or not.
n=[1,3,4,2,6,5]
is_sorted=True
for i in range(len(n)-1):
    if n[i]>n[i+1]:
        is_sorted=False
        break
if is_sorted:
        print("The list is sorted in ascending order")
else:
        print("The list is not sorted in ascending order")

        # (or)

n=[1,3,4,2,6,5]
a=sorted(n)
if a==n:
    print("The list is sorted in ascending order")
else:
    print("The list is not sorted in ascending order")

# Output:-
# The list is not sorted in ascending order

# 3.	Write a Python program to sort a list in ascending order without using the built-in sort() or sorted() functions.
n=[1,3,5,7,8,9,2,4,6]
for x in range(len(n)-1):
    for y in range(len(n)-1):
        if n[x]<n[y]:
            n[x],n[y]=n[y],n[x]
print(n)

# Output:-
# [1, 2, 3, 4, 5, 7, 8, 9, 6]

# 4.	Input : s= ‘abc’     output:  ‘cde’
s="abc"
res=""
for i in s:
    res=res+chr(ord(i)+2)
print(res)

# Output:-
# cde
