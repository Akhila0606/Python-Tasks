# 1. Create a set with elements from 1 to 5. Add elements 6 and 7 to the set in one line.
a={1,2,3,4,5}
a.update({6,7})
print(a)

# Output:-
# {1, 2, 3, 4, 5, 6, 7}

# 2. Given two sets:
#            A = {1, 2, 3, 4, 5}
#            B = {4, 5, 6, 7, 8}
# Find elements that are present in A or B but not both (symmetric difference).
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
s=A.symmetric_difference(B)
print(s)

# Output:-
# {1, 2, 3, 6, 7, 8}

# 3. Remove an element from a set, but avoid error if element doesn't exist.
#  Find maximum and minimum element from a set {5, 8, 12, 3, 15, 7}.
a={5, 8, 12, 3, 15, 7}
a.remove(7)
a.discard(6)
print(a)
print("Maximum Number", max(a))
print("Minimum Number", min(a))

# Output:-
# {3, 5, 8, 12, 15}
# Maximum Number 15
# Minimum Number 3

# 4. Create a set with the values: 10, 20, 30, 40. Then add the value 50 to the set.
a={10, 20, 30, 40}
a.add(50)
print(a)

# Output:-
# {40, 10, 50, 20, 30}

# 5. Remove an element 30 from a set {10, 20, 30, 40, 50} using a set method.
a={10, 20, 30, 40, 50}
a.remove(30)
print(a)

# Output:-
# {50, 20, 40, 10}

# 6. Check whether the number 25 exists in the set {15, 20, 25, 30, 35}.
a={15, 20, 25, 30, 35}
print(25 in a)

# Output:-
# True

# 7. Find the union of two sets:
#            A = {1, 2, 3, 4}
#            B = {3, 4, 5, 6}
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.union(B))

# Output:-
# {1, 2, 3, 4, 5, 6}

# 8. Find the intersection of two sets:
#            A = {10, 20, 30, 40}
#             B = {30, 40, 50, 60}
A = {10, 20, 30, 40}
B = {30, 40, 50, 60}
print(A.intersection(B))

# Output:-
# {40, 30}