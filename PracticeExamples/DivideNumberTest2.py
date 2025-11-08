from DivideNumber2 import DivideNumber

divide = DivideNumber()

# positional argument
result1 = divide.divide_by_four(56)
print(result1)

# default parameter
result2 = divide.default_value()
print(result2)

# keyword argument
result3 = divide.key_value()
print(result3)

# variable-length arguments
result4 = divide.multiple_divisions(8, 16, 32, 56, 56, 78)
print(result4)

# keyword variable-length arguments
result5 = divide.keyword_multiple_divisions(a=12, b=20, c=40)
print(result5)
