class PowerNumber:
    def __init__(self):
        pass

    #positional argument
    def find_power(self,num):
        num **= 5
        return num

    #default argument
    def power_by_default(self,num=8):
        num **= 4
        return num

    #keyward argument
    def power_with_inputs(self,num1,num2):
          return num1 ** 2, num2 ** 3

    #variable length argument
    def powers_from_values(self, *args):
        #return [num ** 2 for num in args]
        result = []
        for num in args:
            squard = num ** 2
            result.append(squard)
        return result

    #keyword varaible length arguments
    def powers_from_items(self, **keyword_arguments):
        dictionary = {}

        for key, val in keyword_arguments.items():
            cube_value = val ** 3
            dictionary[key] = (cube_value)
        return dictionary





