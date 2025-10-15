def greet(name="Guest"):
    print("Hello,", name)
#function call
greet("Ramesh")
greet()

print("----------------------------")

def greet(name="Friend", message="Good Morning"):
    print(f"Hello {name}, {message}!")
#function call
greet("Kiran", "Good Evening")
greet("Ramesh")
greet()

print("-----------------------------")

def add(a=10, b=5):
    print("Sum:", a + b)
#function call
add(3, 7)
add(8)
add()
