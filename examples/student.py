
class Student:
    def __init__(self):
        self.name = ""
        self.age = 0
          #or
        pass

    def set_data(self, name, age):
        self.name = name
        self.age = age

    def get_data(self):
        return (self.name, self.age)  # returning data as a tuple



# Create object
s1 = Student()
s1.set_data("Ravi", 20)
result = s1.get_data()




class Student:
    def __init__(self):
        print("Student object created.")

    def set_data(self, name, age):
        # assigning values to object data members
        self.name = name
        self.age = age

    def display(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)


# Create object → constructor runs automatically
s1 = Student()

# Give values later using method
s1.set_data("Ravi", 20)
s1.display()




class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def get_data(self):
        return(self.name,self.age)

#object creation
s1 = student("ramesh",23)
s2 = student("suresh",24)

print(s1.get_data())
print(s2.get_data())



class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_data(self):
        return(self.name,self.age)

#object creation
s1 = student("rajesh",32)
s1.get_data()

s2 = student("mohan",43)
s2.get_data()

print(s1.get_data())
print(s2.get_data())


        #OR

class student:
    def __init__(self):
        pass
    def set_data(self,name,age):
        self.name=name
        self.age=age

    def get_data(self):
        return(self.name,self.age)


#object creation
s1 = student()
s1.set_data("broke",47)

s2 = student()
s2.set_data("leon",52)



