class LastDigit:
    def __init__(self):
        pass

    def get_number (self,number):
        self.number = number

    def find_Last_Digit(self):
        last =self.number % 10
        return last
    