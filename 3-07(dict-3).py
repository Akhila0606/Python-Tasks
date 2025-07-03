# 1. Invert a dictionary with list values (group keys by their values)
# Input:
# d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
# Output:
# {1: ['a', 'c'], 2: ['b'], 3: ['d']}
# (Hint: Use setdefault method)

d = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
a={}
for x,y in d.items():
    a.setdefault(y,[]).append(x)
print(a)

# Output:-
# {1: ['a', 'c'], 2: ['b'], 3: ['d']}

# 2. Find Max and Min Value in Dictionary
# Input:
# d = {'a': 10, 'b': 5, 'c': 15}
# Output:
# Max Value → 15
# Min Value → 5

d = {'a': 10, 'b': 5, 'c': 15}
max=d['a']
min=d['a']
for i in d.values():
    if max<i:
        max=i
    elif min>i:
        min=i
print("Max Value:", max)
print("Min Value:", min)
#----------(or)-------------
d = {'a': 10, 'b': 5, 'c': 15}
print("Max Value:", max(d.values()))
print("Min Value:", min(d.values()))

# Output:-
# Max Value: 15
# Min Value: 5

# 3. Create a dictionary using dictionary comprehension for the given list of numbers, 
# where:
# • Each number is a key.
# •
# The value is "prime" if the number is prime.
# •
# The value is "notprime" if the number is not prime.
#  Output: {2: 'prime', 3: 'prime', 4: 'notprime', 5: 'prime', 6: 'notprime'}

a={x:"prime" if all(x%y!=0 for y in range(2,x)) else "notprime" for x in range(2,7)}
print(a)

# Output:-
# {2: 'prime', 3: 'prime', 4: 'notprime', 5: 'prime', 6: 'notprime'}

# 4. Create a dictionary from a list of words, keys as words, values as word lengths, but 
# only for words longer than 3 characters
#  List: ["hi", "hello", "world", "is", "great"]

List=["hi", "hello", "world", "is", "great"]
res={}
for i in List:
    if len(i)>3:
        res[i]=len(i)
print(res)
# (or)
List=["hi", "hello", "world", "is", "great"]
res={i:len(i) for i in List if len(i)>3}
print(res)

# Output:-
# {'hello': 5, 'world': 5, 'great': 5}

# 5. Create a dictionary with uppercase letters as keys and their ASCII values as values use 
# dict comprehension .
# Input: letters = ['a', 'b', 'c']
# Expected Output:
# {'A': 65, 'B': 66, 'C': 67}

letters=['a','b','c']
res={}
for i in letters:
    a=i.upper()
    res[a]=ord(a)
print(res)
# (or)
letters=['a', 'b', 'c']
res={chr(ord(i)-32):ord(i)-32 for i in letters}
print(res)

# Output:-
# {'A': 65, 'B': 66, 'C': 67}

# 6. Explain about setdefault function in dictionary data type ?

Setdefault():-
1. Check if a key exists in the dictionary.
2. If it exists, return its value.
3. If it does not exist, add the key with a default value you give.
key - The key you wnat to check or add.
default_value - The value to set if the key doesn't exists.else

Key exists in dictionary- It retutns the existing Value
Key doesn't exist- Adds the key with given default value


# 7. Difference between d[key] and d.get(key)?

1. d[key] -> Direct access
If the exists, it returns the value.
If the key does NOT exist, it gives an error (KeyError).

Example:

d = {'name':'akhila'}
print(d['name'])       # 'akhila' -----works fine
print(d['age'])       # KeyError: 'age'


2. d.get(key) -> Safe access
If the key exists, it returns the value.
If the key does NOT exist, it returns "None" (or a default value you give)

Example:

d = {'name':'akhila'}
print(d.get('name'))          # 'akhila'
print(d.get('age'))          # None (no error)
print(d.get('age', 21))      # 21 (custom default)

# 8. What is the difference between Shallow Copy and Deep Copy in Python? Explain with 
# examples.

-------Shallow Copy--------
A shallow copy creates a new outer object, but the nested (inner) objects are not copied.
Instead, both the original and the copied object share the same inner objects (same memory reference).

Example:

import copy
s=[[1, 2], [3, 4]]
shallow=copy.copy(s)
shallow[0][0]=99
print("s:",original)  # [[99, 2], [3, 4]]
print("shallow:",shallow)    # [[99, 2], [3, 4]]

Explanation:
1. Only the outer list is copied.
2. The inner lists are the same in both.
3. So, a change in one affects the other.

------Deep Copy-------
A deep copy creates a new object and also recursively copies all nested objects.
Both outer and inner objects are completely separate and independent in memory.

Example:
import copy
s=[[1, 2], [3, 4]]
deep=copy.deepcopy(s)
deep[0][0] = 99
print("s:", s)  # [[1, 2], [3, 4]]
print("Deep:", deep)          # [[99, 2], [3, 4]]

Explanation:
1. Both outer and inner lists are copied.
2. So, changing the deep copy doesn't affect the original.

Final Summary Table:
Feature	               Shallow Copy	                 Deep Copy
Definition	       Copies outer object only	       Copies outer and all nested objects
Changes affect?	     Yes (for inner objects)	   No, both are fully independent
Function used	        copy.copy()	                   copy.deepcopy()
