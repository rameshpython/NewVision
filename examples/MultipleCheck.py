class MultipleCheck:
    def __init__(self):
        pass

    def check_multiple(self,num1,num2):

        if num1 % num2 == 0:
            return f"{num1} is a multiple of {num2}"
        else:
            return f"{num1} is not a multiple of {num2}"


