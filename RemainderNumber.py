

class RemainderNumber:
    def __init__(self):
        pass
     #positional arguments
    def find_remainder(self,num):
        num %= 17
        return num

     #default argument
    def default_remainder(self,num = 15):
        num %= 23
        return num

     #keyword argument
    def key_value(self):
        key_num = 27
        result = key_num % 35
        return result

     #varaible length argument
    def variable_length(self, *args):
        return [self.find_remainder(num) for num in args]

     #keyword variable length argument
    def keyword_varriable(self, **kwargs):
        return {k: self.find_remainder(v) for k , v in kwargs.items()}



