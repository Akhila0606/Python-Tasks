# 1. Create a dictionary from two lists:
# a. keys = ['id', 'name', 'age']
# b. values = [101, 'John', 25]
keys = ['id', 'name', 'age']
values = [101, 'John', 25]
res=dict(zip(keys,values))     #Using zip
print(res)

# or
keys = ['id', 'name', 'age']
values = [101, 'John', 25]
p={}
for i in range(len(keys)):
    p[keys[i]]=values[i]
print(p)

# Output:-
# {'id': 101, 'name': 'John', 'age': 25}

# 2. Create a dictionary to store student name and age.
a=[{'name':'akhi','age':21},{'name':'anu','age':22}]
print(a)

# Output:-
# [{'name': 'akhi', 'age': 21}, {'name': 'anu', 'age': 22}]

# 3. Create an empty dictionary and add key-value pairs one by one.
res={}
res['Name']='Akhila'
res['age']=21
res['pin']=101
print(res)

# Output:-
# {'Name': 'Akhila', 'age': 21, 'pin': 101}

# 4. Get the value of key "salary" from this dictionary:
#  EX: employee = {'name': 'John', 'age': 30, 'salary': 50000}
employee = {'name': 'John', 'age': 30, 'salary': 50000}
print(employee['salary'])

# Output:-
# 50000

# 5. Remove the last inserted key-value pair from the dictionary using an appropriate method
employee = {'name': 'John', 'age': 30, 'salary': 50000}
employee.popitem()
print(employee)

# Output:-
# {'name': 'John', 'age': 30}

# 6. Define packing and unpacking in Python. Also, provide one example for both packing and unpacking.

"""Packing: store multiple data types in a single variable(like a tuple or list)"""

res=('akhi',21,'Computer Science')
print(res)

# Output:-
# ('akhi', 21, 'Computer Science')

"""Unpacking: assign multiple from a single collection to variables"""

res=('akhi',21,'Computer Science')
a,b,c=res
print(a)
print(b)
print(c)

# Output:-
# akhi
# 21
# Computer Science