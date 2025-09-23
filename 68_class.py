# Class for Computer Science Student 
class Student: 
    # Class Variable /shared variables
    InstituteName = "the easylearn academy"

    # The init method/constructor 
    def __init__(self, rollno, name): 
        self.rollno = rollno
        self.name = name

# Objects of Student class 
a = Student(101, 'Jay') 
b = Student(102, 'Yashraj') 

# Accessing class variable
print(a.InstituteName) 
print(b.InstituteName) 

print(a.rollno, a.name) 
print(b.rollno, b.name) 

# Access class variable using class name
print(Student.InstituteName) 

# Modify class variable using class name
Student.InstituteName = 'tcs'
print(Student.InstituteName)
