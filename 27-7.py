# 1. Compress a string using character counts.
# Input: "aabbbcc" → Output: "a2b3c2"

a="aabbbcc"
print(a)
res=""
for i in a:
    if i not in res:
        s=a.count(i)
        res+=i+str(s)
print(res)

# Output:-
# aabbbcc
# a2b3c2

# 2. Convert a string to title case without using .title().
# Input: "python is fun" → Output: "Python Is Fun"

a="python is fun"
print(a)
w=a.split()
res=""
for i in w:
    res+=i.capitalize()+" "
print(res.strip())

# Output:-
# python is fun
# Python Is Fun

# 3. Check whether two strings are anagrams of each other.

s1=input("enter a string:").lower()
s2=input("enter a string:").lower()
if sorted(s1)==sorted(s2):
    print("Anagrams")
else:
    print("Not Anagrams")

# Output:-
# enter a string:listen
# enter a string:silent
# Anagrams
# (or)
# enter a string:hello
# enter a string:world
# Not Anagrams

# 4. Convert a string "1a2b3c" to "abc123".

s="1a2b3c"
print(s)
letters=""
digits=""
for i in s:
    if i.isalpha():
        letters+=i
    if i.isdigit():
        digits+=i
res=letters+digits
print(res)

# Output:-
# 1a2b3c
# abc123

# 5. Extract all numbers from a string and calculate their sum.
#  "abc12xyz34" → Output: 46

p="abc12xyz34"
print(p)
res=0
for i in range(len(p)-1):
    if p[i].isdigit() and p[i+1].isdigit():
        res+=int(p[i]+p[i+1])
print(res)

# Output:-
# abc12xyz34
# 46

# 6. Sort a list in ascending and descending order with out using sort? 

s=[5,2,4,3,1]
print(s)
for i in range(len(s)):
    for j in range(len(s)-1-i):
        if s[j]>s[j+1]:
            s[j],s[j+1]=s[j+1],s[j]
print("Ascending order:", s)
for x in range(len(s)):
    for y in range(len(s)-1-x):
        if s[y]<s[y+1]:
            s[y],s[y+1]=s[y+1],s[y]
print("Descending order:", s)

# Output:-
# [5, 2, 4, 3, 1]
# Ascending order: [1, 2, 3, 4, 5]
# Descending order: [5, 4, 3, 2, 1]

# 7. Find the second largest number in a list.

s=[10,20,30] 
print(s)
max1=0
max2=0
for i in s:
    if i>max1:
        max2=max1
        max1=i
    elif max1>i>max2:
        max2=i
print("Second largest number:", max2)

# Output:-
#[10, 20, 30]
# Second largest number: 20

# 8. Find the intersection and union of two lists.

#intersection
s1=[1, 2, 3, 4]
s2=[3, 4, 5, 6]
res=[]
for i in s1:
    if i in s2 and i not in res:
        res.append(i)
print("Intersection:", res)
#union
s1=[1, 2, 3, 4]
s2=[3, 4, 5, 6]
a=[]
for i in s1:
    if i not in a:
        a.append(i)
for j in s2:
    if j not in a:
        a.append(j)
print("Union:", a)

# (or)

s1=[1, 2, 3, 4]
s2=[3, 4, 5, 6]
intersection=list(set(s1)&set(s2))
print("Intersection:", intersection)
union=list(set(s1)|set(s2))
print("Union:", union)

# Output:-
# Intersection: [3, 4]
# Union: [1, 2, 3, 4, 5, 6]

# 9. Print all prime numbers from a list.

n=[2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for i in n:
    if i>1:   #Numbers greater than 1 that have only two factors — 1 and the number itself.
        is_prime=True
        for j in range(2,i):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
            print(i, end=" ")

# Output:-
# 2 3 5 7 11 

# 10. Find if a number is Armstrong or not.

k=153
h=k
res=0
n=len(str(k))
while k>0:
    digit=k%10
    k//=10
    res+= digit**n  
print(res)
if h==res:
    print("It is a Armstrong number")
else:
    print("It is not a Armstrong number")

# Output:-
# 153
# It is a Armstrong number

# 11. Count number of vowels in a string using while.

s="Education"
print(s)
vowels="aeiou"
i=0
count=0
while i<len(s):
    if s[i] in vowels:
        count+=1
    i+=1
print("Number of vowels:", count)

# Output:-
# Education
# Number of vowels: 4

# 12. Print multiplication table in reverse order.

n=5
for i in range(10,0,-1):
    print(n, "X", i, "=", i*n)

# Output:-
# 5 X 10 = 50
# 5 X 9 = 45
# 5 X 8 = 40
# 5 X 7 = 35
# 5 X 6 = 30
# 5 X 5 = 25
# 5 X 4 = 20
# 5 X 3 = 15
# 5 X 2 = 10
# 5 X 1 = 5

# 13. Count how many times digit 7 appears between 1 to 100.

count=0
for i in range(1,101):
    if "7" in str(i):
        count+=1
print("Digit 7 appears between 1 to 100:", count)

# Output:-
# Digit 7 appears between 1 to 100: 19

# 14. Create a countdown timer (like 10 → 0) using while loop.

import time
count=10
while count>=0:
    print(count)
    time.sleep(1)
    count-=1
print("Time is up")

# Output:-
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0
# Time is up

# 15. Replace all negative numbers in a list with 0. Using list comprehention?

n=[4, -2, 7, -9, 0, 3, -5]
res=[0 if x<0 else x for x in n]
print(res)

# Output:-
# [4, 0, 7, 0, 0, 3, 0]

# 16. Write Function to check if a list is sorted or not.

def is_sorted(list):
    return list==sorted(list)
print(is_sorted([1,2,3,4,5]))
print(is_sorted([3,2,1]))
print(is_sorted([10,20,30,40]))

# Output:-
# True
# False
# True

# 17. Sort a dictionary by values

a={"a":3, "b":2, "c":1}
print(a)
res=sorted(a.values())
print("Sorted dictionary values:", res)

# Output:-
# {'a': 3, 'b': 2, 'c': 1}
# Sorted dictionary values: [1, 2, 3]

# 18. Store student names and marks in a dictionary and print each student’s result.

s={
    "Akhila":85,
    "Anjali":100,
    "Anusha":95,
}
for i,j in s.items():
    print(f"{i} scored {j} marks")

# Output:-
# Akhila scored 85 marks
# Anjali scored 100 marks
# Anusha scored 95 marks

# 19. Write a lambda function that takes two numbers and returns a tuple containing:
# i. Their sum
# ii. Their product
# iii. Their difference

res=lambda x,y:(x+y, x*y, x-y)
print(res(10,5))

# Output:-
# (15, 50, 5)



