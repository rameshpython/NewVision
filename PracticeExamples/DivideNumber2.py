class DivideNumber:
    def __init__(self):
        pass

    # positional argument
    def divide_by_four(self, num):
        num /= 4
        return num

    # default argument
    def default_value(self, num=20):
        num /= 4      # directly divide here (no self call)
        return num

    # keyword argument
    def key_value(self):
        key_num = 24
        result = key_num / 4
        return result

    # variable-length arguments (*args)
    def multiple_divisions(self, *args):
        return [self.divide_by_four(num) for num in args]

    # keyword variable-length arguments (**kwargs)
    def keyword_multiple_divisions(self, **kwargs):
        return {k: self.divide_by_four(v) for k, v in kwargs.items()}





    # variable-length arguments (*args)
#    def multiple_divisions(self, *args):
#        results = []
#        for num in args:
#            results.append(num / 4)
#        return results

    # keyword variable-length arguments (**kwargs)
#    def keyword_multiple_divisions(self, **kwargs):
#        result_dict = {}
#        for k, v in kwargs.items():
#            result_dict[k] = v / 4
#        return result_dict