# 1. Print All Duplicate Characters in a String
a="akhila"
s=""
res=""
for i in a:
    if i not in s:
        s=s+i
    else:
        res=res+i
print(res)

#Output:-
# a

# 2. Replace Vowels with ‘*’
a="akhila"
res=""
for i in a:
    if i in "aeiouAEIOU":
        res=res+"*"
    else:
        res=res+i
print(res)

# Output:-
# *kh*l*

# 3. Convert a Snake_Case String to CamelCase.
a="convert_string"
res=""
for i in range(len(a)):
    if a[i]=="_":
        continue
    elif i>0 and a[i-1]=="_":
        res+=a[i].upper()
    else:
        res=res+a[i]
print(res)

# Output:-
# convertString
     

# 4. Use reduce() to Find Product of List Elements
from functools import reduce
s=[10,20,30,40]
print(reduce(lambda x,y:x*y, s))

# Output:-
# 240000
