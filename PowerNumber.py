class PowerNumber:
    def __init__(self):
        pass

    #positional argument
    def find_power(self,num):
        num **= 5
        return num

    #default argument
    def find_default(self,num=8):
        num **= 4
        return(num)

    #keyward argument
    def key_value(self):
        key_num = 43
        key_num **= 6
        return key_num

    #varaible length argument
    def varaiable_length(self, *args):
        return [self.find_power(num) for num in args]

    #keyword varaible length arguments
    def keyword_varriable(self, **kwargs):
        return {k: self.find_power(v) for k , v in kwargs.items()}

