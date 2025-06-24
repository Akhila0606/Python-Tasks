# 1.Write a Python program that takes an amount n = 5200 and breaks it down into the minimum number of currency notes available in                         denominations of 500, 200, 100, 50, 20, 10, and 1 rupees.
#                Output: 10 500rupees notes and 1 200rupees notes
n=5200
a=[500,200,100,50,20,10]
res=[]
for i in a:
    digit=n//i
    if digit>0:
        res.append(f" {digit} {i} rupees notes")
        n%=i
print(res)

# Output:-
# [' 10 500 rupees notes', ' 1 200 rupees notes']

# 2. Write a Python program to keep asking the user to enter a password until they enter the correct
while True:
    m=input("Enter a password:")
    if m=="akhi123":
        print("Login succesfully")
    else:
        print("worong password")

# Output:-
# Enter a password:akhi123 
# Login succesfully

# 3. Convert a 2D list into a flat 1D list using list comprehension.
m=[[1,2],[3,4],[5,6]]
res=[x for i in m for x in i]
print(res)

# Output:-
#  [1, 2, 3, 4, 5, 6]

# 4. Given a string, use list comprehension to create a list of all characters, excluding vowels.
a="Hello World"
res=[x for x in a if x not in "aeiou/AEIOU"]
print(res)

# Output:-
# ['H', 'l', 'l', ' ', 'W', 'r', 'l', 'd']

# 5. From a given list of words, extract only those that start with a vowel (a, e, i, o, u).
#   Example:  words = ["functions", "loops", "oops", "exception", "as"]
words= ["functions","loops","oops","exception","as"]
res=[x for x in words if x[0] in "aeiouAEIOU"]
print(res)

# Output:-
# ['oops', 'exception', 'as']