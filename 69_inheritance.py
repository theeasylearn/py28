class Person: #parent/super/base class 
    def walk(self):
        print("I can walk")
    def talk(self):
        print("I can talk")
    def eat(self):
        print("I can eat")
class Student(Person): #child/sub/derived class
    def read(self):
        print("I can read")
    def write(self):
        print("I can write")
    def WhatICanDo(self):
        #calling parent class method 
        super().walk()
        super().talk()
        super().eat()
        self.read()
        self.write()
#creating object of parent class 
p1 = Person()
p1.walk()
p1.talk()
p1.eat() #creating object of child class
s1 = Student()
s1.WhatICanDo()
s1.walk()
s1.read()
