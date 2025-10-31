#Write a program to divide a number by 4 using /=.
class DivideNumber:
    def __init__(self):
        pass

#    def divide_by_four(self,num = 20):
#        num /= 4
#        return num

    #positional argument
    def divide_by_four(self,num):  # method that divides any number by 4
        num /= 4
        return num

    #default argument
    def default_value(self,num=20): # method that uses a default value
        return self.divide_by_four(num) # call first method using default
           #0r
        #return  f"After divide by 4 the number is {num}"

    #keyword argument
    def key_value(self):
        key_num = 24
        return self.divide_by_four(num=key_num)

    # variable-length arguments (*args)
    def multiple_divisions(self, *args):
        return [self.divide_by_four(num) for num in args]

    # keyword variable-length arguments (**kwargs)
    def keyword_multiple_divisions(self, **kwargs):
        return {k: self.divide_by_four(v) for k, v in kwargs.items()}






