# 1. Delete a list of keys from a dictionary
# sample_dict = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"}
# # Keys to remove
# keys = ["name", "salary"]
sample_dict = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"}
# Keys to remove
keys = ["name", "salary"]
for i in keys:
    sample_dict.pop(i)
print(sample_dict)

# Output:-
# {'age': 25, 'city': 'New york'}

# 2. Count the frequency of each character in a given string using a dictionary.
a="python programming"
res={}
for i in a:
    res[i]=a.count(i)
print(res)

# Output:-
# {'p': 2, 'y': 1, 't': 1, 'h': 1, 'o': 2, 'n': 2, ' ': 1, 'r': 2, 'g': 2, 'a': 1, 'm': 2, 'i': 1}

# 3. Swap keys and values in a dictionary.
a={1:'a',2:'b',3:'c',4:'d'}
res={}
for i,j in a.items():
    res[j]=i
print(res)

# Output:-
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 4. Write a program to sum all the values in a dictionary.
s={'a': 6, 'b': 11, 'c': 25, 'd': 100}
sum=0
for i in s.values():
    sum+=i
print(sum)

# Output:-
# 142

# 5. Create a nested dictionary for student details (name, roll, marks).
d={
    'CSE-student':{'name':'Akhila','roll-no':567,'marks':78},
    'ECE-student':{'name':'Anusha','roll-no':428,'marks':88},
    'CSE-A':{'name':'Anil','roll-no':548,'marks':80}
   }
print(d)

# Output:-
# {'CSE-student': {'name': 'Akhila', 'roll-no': 567, 'marks': 78}, 
#  'ECE-student': {'name': 'Anusha', 'roll-no': 428, 'marks': 88}, 
#  'CSE-A': {'name': 'Anil', 'roll-no': 548, 'marks': 80}}

# 6. Convert a dictionary to a list of tuples.
s={"name": "Kelly","age": 25, "salary": 8000, "city": "New york"}
res=[]
for i in s.items():
    res.append(i)
print(res)

# Output:-
# [('name', 'Kelly'), ('age', 25), ('salary', 8000), ('city', 'New york')]

# 7. Write a program to store names as keys and their lengths as values.
s={'sita','ramudu','anjali','radha','krishna','anusha'}
res={}
for i in s:
    res[i]=len(i)
print(res)

# Output:-
# {'ramudu': 6, 'radha': 5, 'anjali': 6, 'krishna': 7, 'anusha': 6, 'sita': 4}

# 8. Create a dictionary for numbers 1 to 5, where the value is "even" if the number is even, and 
# "odd" if the number is odd
# Expected Output:
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}
a={}
for i in range(1,6):
    if i%2==0:
        a[i]="even"
    else:
        a[i]="odd"
print(a)

# Output:-
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

# 9. Create Reverse Word Dictionary
# Given list of words:
# words = ["cat", "dog", "bat"]
# Create a dictionary with words as keys and their reversed strings as values
# Expected Output:
# {'cat': 'tac', 'dog': 'god', 'bat': 'tab'}
words = ["cat", "dog", "bat"]
a={}
for i in words:
    a[i]=i[::-1]
print(a)

# Output:-
# {'cat': 'tac', 'dog': 'god', 'bat': 'tab'}