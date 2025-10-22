class DoubleNumber:
    def __init__(self):#empty constructor
        self.number = int(input("Enter a number: "))

    def find_double(self):
        print("Double of the number is:", self.number * 2)

d1 = DoubleNumber()
d1.find_double()



class TripleNumber:
    def __init__(self):#empty constructor
        self.number =float(input("Enter a number: "))

    def find_Triple(self):
        print("Triple of the number is:",self.number * 3)

d1 = TripleNumber()
d1.find_Triple()





class DoubleNumber:
    def find_double(self, number):
        print("Double of the number is:", number * 2)

# Create object
d1 = DoubleNumber()
d1.find_double(55)   # pass the number here



class DoubleNumber:
    def __init__(self):
        def find_double(self,number):
            print("Double of the number is:",self,number*2)
#create object
d1 =DoubleNumber()
#d1.find_double()





