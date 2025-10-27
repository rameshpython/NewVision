class Expression:
    def __init__(self):
        pass

    def get_data(self,x,y):
        self.x = x
        self.y = y

    def calculate(self):
        result = (self.x + self.y) * (self.x - self.y)
        return result


