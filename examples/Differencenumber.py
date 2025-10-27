class Differencenumber: #using without initialazation
    self.number1 = num1
    self.number2 = num2

    def find_differencenumber(self):
        difference = self.number1 - self.number2
        print("The difference between the two numbers is:", difference)

#create an object of the class
d1 = Differencenumber()

#call the method
d1.find_differencenumber()