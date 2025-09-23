class Person():
    # __init__ is known as the constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class Employee(Person):
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber) # invoking the __init__ of the parent class
        self.salary = salary
        self.post = post
    def display(self): #method overriding
        super().display() #calling parent class method display
        print(self.salary)
        print(self.post)
p = Person('jiya', 1234) # parent class object
p.display() # calling a function of the class Person using its instance
e = Employee("Rahul", 101, 125000, 'Developer') # child class object
e.display()
