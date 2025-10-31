from PowerNumber import PowerNumber

powernumber = PowerNumber()

#positional argument
power_result1 = powernumber.find_power(8)
print(power_result1)

#default argument
power_result2 = powernumber.find_default(16)
print(power_result2)

#keyward argument
power_result3 = powernumber.key_value()
print(power_result3)

#variable length argument
power_result4 = powernumber.varaiable_length(12, 34, 13, 14, 15)
print(power_result4)

#keyword varaible length argument
power_result5 = powernumber.keyword_varriable(a=23, b=13, c=14, d=16)
print(power_result5)



