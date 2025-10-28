class Expression2:
    def __init__(self):
        pass

    def calculate(self,a,b,c):
        result = (a+b) ** c - b * c + a % b
        return result

