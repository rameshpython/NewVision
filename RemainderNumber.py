

class RemainderNumber:
    def __init__(self):
        pass
     #positional arguments
    def find_remainder(self,num):
        num %= 17
        return num

     #default argument
    def remainder_by_default(self,num = 15):
        num %= 23
        return num

     #keyword argument
    def remainder_by_value(self, num):
        result = num % 35
        return result

     #varaible length argument
    def  remainders_from_values(self, *args):
        return [num % 18 for num in args]

     #keyword variable length argument
    def remainders_from_items(self, **kwargs):
        return {k : v % 27  for k , v in kwargs.items()}





