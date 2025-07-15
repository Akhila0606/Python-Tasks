# 1.	Create a class Person with instance attributes name and age. Write an instance method display() that prints the name and age.
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:", self.name)
        print("Agea:", self.age)
obj=person("Akhila",21)
obj.display()

# Output:-
# Name: Akhila
# Agea: 21

# 2.	Create a class Employee with attributes name and salary. Write an instance method update_salary() to update the salary.
class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def update_salary(self,name,money):
        if self.name==name:
            self.salary+=money
            print("Updated Salary:", self.salary)
obj=employee("Ram",0)
obj.update_salary("Ram",20000)
obj.update_salary("Ram",30000)

# Output:-
# Updated Salary: 20000
# Updated Salary: 50000

# 3.	Create a class BankAccount with   “balance attribute deposit() and withdraw()” instance methods.
class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self,balance,amount):
        if self.balance==balance:
            self.balance+=amount
            print("Deposit amount:",self.balance)
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Withdraw Amount:",self.balance)
    def show(self):
        print("Present balance:",self.balance)
obj=BankAccount(1000)
obj.deposit(1000,2000)
obj.withdraw(1500)
obj.show()

# Output:-
# Deposit amount: 3000
# Withdraw Amount: 1500
# Present balance: 1500

# 4.	Create a class Student with  Attributes  name, marks (list) Method: average() → returns average marks.
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        total=sum(self.marks)
        count=len(self.marks)
        return total / count
    def show(self):
        print("Name:",self.name)
        print("Marks:",self.marks)
obj=Student("Akhila",[50,60,70])
obj.show()
print("Average Marks:",obj.average())

# Output:-
# Name: Akhila
# Marks: [50, 60, 70]
# Average Marks: 60.0

# 5.	Difference Between Class Method and Instance Method.

# Instance Method:-

# A method that works with individual objects (instances) of a class.
# First parameter is always self, which refers to the object itself.

# Usage:
# Can access and modify instance variables (like self.name).
# Called using the object.

# Example:
class Student:
    def __init__(self, name):
        self.name = name
    def method(self):  # instance method
        print("Hello", self.name)
s = Student("Akhila")
s.method()  

# Output: Hello Akhila

# Class Method:-

# Works with the class itself, not individual objects.
# First parameter is cls, referring to the class.
# Declared with the @classmethod decorator.

# Usage:
# Can access or modify class variables (shared by all instances).
# Can be used to create factory methods (like alternative constructors).

# Example:
class Student:
    school = "JNTUH"  # class variable
    def __init__(self, name):
        self.name = name
    @classmethod
    def method(cls):  # class method
        print("School:", cls.school)
Student.method()  

# Output: School: JNTUH
