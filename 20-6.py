# 1. Write a Python program to print the word with the maximum length from the list m = ['python', 'java', 'c++', 'developer']
m=['python','java','c++','developer']
res=""
for i in m:
    if len(i)>len(res):
        res=i
print(res)

# Output:-
# developer

# 2. Given a list and a target number, return all pairs that sum to the target.
l=[1,2,3,6,2,2,4,3,4,7,8,3,0]
n=8
for i in range (len(l)-1):
    if l[i]+l[i+1]==n:  
        print(l[i],l[i+1])

# Output:-
# 6 2

# 3. Write a program to remove duplicate elements from a list.
n=[1,2,3,2,4,1,5,3]
res=[]
for i in n:
    if i not in res:
        res.append(i)
print(res)

# Output:-
# [1, 2, 3, 4, 5]

# 4. Write a Python program to print the common elements between two given lists.
l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
res=[]
for i in l1:
    if i in l2 and i not in res:
        res.append(i)
print(res)

# Output:-
# [4, 5]

# 5. Write a Python program to move all 0's in the list k = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0] to the end of the list?
k=[1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0]
res=[]
for i in k:
    if i==0:
        k.remove(i)
        res.append(i)
print(k+res)

# Output:-
# [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]