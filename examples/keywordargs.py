def  greet(name,message):
    print(f"Hello{name},{message}!")

#function call
greet("Ramesh","Good morning")
print("----------------------------------------")

def greet(name, message):
    print(f"Hello {name},{message}!")
#function call
greet(message="Good Evening", name="Kiran")


def greet(name, message):
    print("Hello {},{}!".format(name,message))
#function call
greet(message="Good Evening", name="Kiran")

print("--------------------------------------------")

def student_info(name, age, course):
    print(f"Name: {name}, Age: {age}, Course: {course}")

#function call
student_info("Ravi", age=21, course="Python")
student_info("suresh",23,course="python")
student_info(name="Ravi", age=21, course="Python")

print("----------------------------------------------")

def create_account(username, email,passwoed, admin=False):
    print(f"Username: {username}, Email: {email}, Admin: {admin}")

# function call
create_account(username="ramesh", email="ramesh@gmail.com", password="12345", admin=True)

