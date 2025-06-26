# 1. nums = [5, 12, 17, 24, 35, 40, 55]
#   Create a tuple containing only numbers that are divisible by 5 using comprehension.
n=[5,12,17,24,35,40,55]
res=tuple(x for x in n if x%5==0)
print(res)

# Output:-
# (5, 35, 40, 55)

# 2. Given a string: "HelloWorld" Create a tuple of all uppercase letters present in the string using comprehension.?
t="HelloWorld"
res=tuple(i for i in t if i.isupper())
print(res)

# Output:-
# ('H', 'W')

# 3. marks = [55, 72, 48, 90, 67]
#  Create a tuple where each element is "Pass" if marks are >= 50 else "Fail" using comprehension.?
n=[55,72,48,90,67]
res=tuple("Pass" if x>=50 else "Fail" for x in n)
print(res)

# Output:-
# ('Pass', 'Pass', 'Fail', 'Pass', 'Pass')

# 4. Given a sentence: "Python is powerful and easy to learn"
#  Create a tuple of words that have more than 4 characters using comprehension.
a="Python is powerful and easy to learn"
res=tuple(x for x in a.split() if len(x)>4)
print(res)

# Output:-
# ('Python', 'powerful', 'learn')

# 5. students = [("Alice", 85), ("Bob", 45), ("Charlie", 60), ("David", 30)]
#  Create a tuple containing names of students who scored 50 or more using comprehension
s=[("Alice", 85), ("Bob", 45), ("Charlie", 60), ("David", 30)]
res=tuple(x[0] for x in s if x[1]>50)
print(res)

# Output:-
# ('Alice', 'Charlie')