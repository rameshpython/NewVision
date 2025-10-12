def greet(name,message):
    print(message,name)

#function call
greet("ramesh","hello")
print("----------------------------------------------------------")


def add(a,b=5):
    return a+b
print(add(10))
print(add(10,20))

def blender(fruit1, fruit2):  # parameters
    print("Making juice with", fruit1, "and", fruit2)

blender("apple", "mango")     # arguments
print("-----------------------------------------------------------")

def show_info(name,age):
    print("name:",name)
    print("age:",age)

#functon call
show_info("Ramesh",25)
print("------------------------------------------------------------")

def student_info(name, age, course, city):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)
    print("City:", city)

student_info("Ramesh", 20, "Python", "Hyderabad")
print("---------------------------------------------------------------")

def add(a, b, c):
    print(a, b, c)

add(10, 20, 30)
#a=10,b=20,c=30
#so order matters in positional arguments
print("-----------------------------------------------------------------")

def display(a, b):
    print("a =", a, "type:", type(a))
    print("b =", b, "type:", type(b))
#function call
display(10, "Ramesh")

#parameters are only placeholders and we call them as varaiables
#output  a = 10 type: <class 'int'>
#        b = Ramesh type: <class 'str'>
print("------------------------------------------------------------------")

def mix_data(num, text, data):
    print(num * 2)
    print(text.upper())
    print(len(data))

mix_data(5, "hello", [1, 2, 3, 4])
print("-----------------------------------------")

def greet():
    print("Hello World!")

greet()
print("------------------------------------------")

def greet(name, age):
    print(f"Hello {name}, your age is {age}")

greet("Ravi", 15)
print("-------------------------------------------")

def get_pi():
    return 3.14159

print(get_pi())
#function without argument only with empty parameter and return as 3.14159
print("----------------------------------------------")
def add(a, b):
    return a + b

print(add(5, 10))
#function with positional argument and return as result