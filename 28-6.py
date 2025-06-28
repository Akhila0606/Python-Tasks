# 1. Write a Python program to rotate a list to the right by k steps.
l=[1,2,3,4,5]
k=2
print(l[-k:] + l[:-k])

# Output:-
# [4, 5, 1, 2, 3]

# 2. Write a Python program to find the sum of prime digits in the number L = 123456.
l= 123456
total=0
prime_no=[2,3,5,7]
while l>0:
    digit=l%10
    if digit in prime_no:
        total+=digit
    l=l//10
print("Sum of prime digits is", total)

# Output:-
# Sum of prime digits is 10

# 3. Write a Python program to find the sum of even digits in the number M = 65897.
m=65897
total=0
while m>0:
    digit=m%10
    if digit%2==0:
        total+=digit
    m//=10
print("Sum of even digits is:", total)

# Output:-
# Sum of even digits is: 14

# 4. Write a Python program to calculate the sum of the largest elements from each row of a 2D.
# list. EX: M=[[1,2,3],[4,5,6],[7,8,9]] output: 24
m=[[1,2,3],[4,5,6],[7,8,9]]
res=0
for i in m:
    digit=max(i)
    res+=digit
print(res)

# Output:-
# 18

# 5. Write a Python program to find the product of all elements in a list.
n=[2,3,4,5]
product=1
for i in n:
    product*=i
print("product of all elements in a list:", product)

# Output:-
# product of all elements in a list: 120

# 6. Write a Python program to check whether a given number is an Armstrong number or not.
# EX: K=153
k=153
h=k
total=0
res=len(str(k))
while k>0:
    digit=k%10
    total+=digit**res
    k//=10
if total==h:
    print(h, "It is an Armstrong number")
else:
    print(h, "Not an Armstrong number")

# Output:-
# 153 It is an Armstrong number

# 7. Write a Python program to check whether a given number is a Perfect number or not.
# Perfect number: sum of all factors of a given number
n=28
total=0
for i in range(1,n):
    if n%i==0:
        total+=i
if total==n:
    print(n, "It is a perfect number")
else:
    print(n, "not a perfect number")

# Output:-
# 28 It is a perfect number