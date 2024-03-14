# class Employee:
#     def __init__(self,eno,ename):
#          self.eno = eno
#          self.ename = ename
#          print("Constructor Execution...")
#     def display(self):
#          print("Employee No : ", self.eno)
#          print("Employee Name : ", self.ename)
 
        
# e1 = Employee(100,"Durga")
# e1.display()

# ## Lambda

# def func(a):
#      return a+5

func = lambda a: a+5
square = lambda x: x**x
sum = lambda a, b, c: a+b+c

x = 3
print(func(x)) # Prints 8
print(square(x)) # Prints 9
print(sum(x, 1, 2)) # Prints 6

# ### map()

def square(num):
    return num*num

l = [1, 2, 4]

# Method 1
l2 = []
for item in l:
    l2.append(square(item))
print(l2)

# Method 2
print(list(map(square, l)))

# ## filter()

def greater_than_5(num):
    if num > 5:
        return True
    else:
        return False

g10 = lambda num: num>10

l = [1, 2, 3, 4, 5, 6, 7, 8, 89, 98]
print(list(filter(greater_than_5, l)))
print(list(filter(g10, l)))

from functools import reduce

sum = lambda a, b: a+b

l = [1, 2, 3, 4]
val = reduce(sum, l)
print(val)

class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()
harry.salary = 300
rajni.salary = 400

print(harry.company)
print(rajni.company)
Employee.company = "YouTube"
print(harry.company)
print(rajni.company)
print(harry.salary)
print(rajni.salary)

class Employee:
    company = "Google"
    salary = 100

harry = Employee()
rajni = Employee()

# Creating instance attribute salary for both the objects
# harry.salary = 300
# rajni.salary = 400
harry.salary = 45
print(harry.salary)
print(rajni.salary)


# Below line throws an error as address is not present in instance/class 
# print(rajni.address) 

class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

harry = Employee()
harry.salary = 100000
harry.getSalary() # Employee.getSalary(harry)

class Employee:
    company = "Google"

    def getSalary(self, signature):
        print(f"Salary for this employee working in {self.company} is {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

harry = Employee()
harry.salary = 100000
harry.getSalary("Thanks!") # Employee.getSalary(harry)
harry.greet() # Employee.greet()
harry.time()



class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"
    company = "Youtube"

    def getLanguage(self):
        print(f"The language is {self.language}")
    
    def showDetails(self):
        print("This is an programmer")


e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)



class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1
        return self.level

class Employee:
    company = "Visa"
    eCode = 120


class Programmer(Freelancer, Employee):
    name = "Rohit"
      
p = Programmer()
p.upgradeLevel()
print(p.company)


