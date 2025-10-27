class Difference:
    def __init__(self):
        # constructor to take input from the user
        self.num1 = float(input("Enter the first number: "))  # converted to global varaiable
        self.num2 = float(input("Enter the second number: "))

    def find_difference(self):
        # method to calculate and display difference
        difference = self.num1 - self.num2
        print("The difference between the two numbers is:", difference)


# create an object of the class
d1 = Difference()

# call the method
d1.find_difference()


class Difference:
    def __init__(self, num1, num2):
        self.number1 = num1  # converted to global varaiable
        self.number2 = num2

    def find_difference(self):
        difference = self.number1 - self.number2
        print("The difference between the two numbers is:", difference)


# create an object of the class
d1 = Difference(10, 5)

# call the method
d1.find_difference()


class Difference:  # without initialization
    def find_difference(self):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        difference = num1 - num2
        print("The difference between the two numbers is:", difference)


# create an object of the class
d1 = Difference()

# call the method
d1.find_difference()

