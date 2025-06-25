# 1. rotate a list by k positions.
# left
v=[1,2,3,4,5]
k=2
k=k%len(v)
print(v[k:]+v[:k])
# Right
v=[1,2,3,4,5]
k=2
k=k%len(v)
print(v[-k:]+v[:-k])

# Output:-
# [3, 4, 5, 1, 2]
# [4, 5, 1, 2, 3]

#------------------------------------------------------------------

# 2. Find the second largest element in a list without sorting.
s=[10,20,30] 
max1=0
max2=0
for i in s:
    if i>max1:
        max2=max1
        max1=i
    elif max1>i>max2:
        max2=i
print("second largest:", max2)

# Output:-
# second largest: 20

#------------------------------------------------------------------

# 3. Move all zeroes to the end of the list while maintaining the order.
s = [0,4,0,3,0,2,0,1]
res=[]
for i in s:
        if i==0:
            s.remove(i)
            res.append(i)
print(s+res)

# Output:-
# [4, 3, 2, 1, 0, 0, 0, 0]

#------------------------------------------------------------------

# 4. Remove duplicates from a list without using set().
s = [1, 2, 3, 2, 4, 1, 5, 3]
list=[]
for i in s:
    if i not in list:
        list.append(i)
print(list)

# Output:-
# [1, 2, 3, 4, 5]

#------------------------------------------------------------------

# 5. Count the frequency of each element in a list.
s = [1, 2, 3, 2, 4, 1, 5, 3]
v=[]
for i in s:
    if i not in v:
        v.append(i)
for i in v:
    print(i,":",s.count(i),end="     ")

# Output:-
# 1 : 2     2 : 2     3 : 2     4 : 1     5 : 1 

#------------------------------------------------------------------

# 6. Find the maximum product of two elements in a list.
l=[6,100,2,3,5,4,6,3,3]
max=0
for i in range(len(l)-1):
    a=l[i]*l[i+1]
    if a >max:
        max=a
    else:
        max=max
print(max)

# Output:-
# 600

#------------------------------------------------------------------

# 7. Reverse a list without using built-in reverse functions.
s=[1,2,3,4,5]
reverse=[]
for i in range(len(s)-1,-1,-1):   #starts from the last index and goes backward.
    reverse.append(s[i])
print(reverse)
# using sawapping
s=[1,2,3,4,5]
start=0
end=len(s)-1   # = 4
while start<end:
    s[start], s[end]=s[end], s[start]   #  start = 0, end = 4     s[0], s[4] = s[4], s[0] → 1 and 5 are swapped
    start+=1   # Move from left to center
    end-=1     # Move from right to center
print(s)

# Output:-
# [5, 4, 3, 2, 1]

#------------------------------------------------------------------

# 8. Check if a list is a palindrome.
p=[1,2,3,2,1]
h=p
res=[]
for i in range(len(p)-1,-1,-1):
        res.append(p[i])
if res==h:
    print("Palindrome")
else:
    print("not a paindrome")

# Output:-
# Palindrome

#------------------------------------------------------------------

# 9. Find the common elements between two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common=[]
for i in list1:
    if i in list2 and i not in common:
        common.append(i)
print(common)
# using set() method
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common=(set(list1)&set(list2))
print(common)

# Output:-
# [3, 4, 5]