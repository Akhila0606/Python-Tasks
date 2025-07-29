# 1. With use of decorator write prime number range of 20.

def fun2(fun):
    def inner(n):
        for i in range(n):
            if i>1:
                is_prime=True
                for j in range(2,i):
                    if i%j==0:
                        is_prime=False
                        break
                if is_prime:
                    print(i,end=" ")
    return inner
@fun2
def fun():
    print("This is prime number")
fun(20)

# Output:-
# 2 3 5 7 11 13 17 19

# 2. With use of decorator write factors program.

def fun2(fun):
    def inner(a):
        for i in range(1,a):
            if a%i==0:
                print(i,end=" ")
    return inner
@fun2
def fun():
    print("These are Factors")
fun(20)

# Output:-
# 1 2 4 5 10 

# 3. With use of decorator write multiplication table.

def fun2(fun):
    def inner(a):
        for i in range(1,11):
            print(a,"X",i,"=",a*i)
    return inner
@fun2
def fun():
    print("Multiplication Table")
fun(6)

# Output:-
# 6 X 1 = 6
# 6 X 2 = 12
# 6 X 3 = 18
# 6 X 4 = 24
# 6 X 5 = 30
# 6 X 6 = 36
# 6 X 7 = 42
# 6 X 8 = 48
# 6 X 9 = 54
# 6 X 10 = 60