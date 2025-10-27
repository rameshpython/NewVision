class swapNumbers:
    def __init__(self):
        pass

    def swap(self,a,b):



#In swap case we use formula without using third variable by Arithmetic
        a = a + b
        b = a - b
        a = a - b
        return a,b



