from RemainderNumber import RemainderNumber

remainder = RemainderNumber()

#positional argument
remainder_result1 = remainder.find_remainder(26)
print(remainder_result1)

#default argument
remainder_result2 = remainder.remainder_by_default(13)
print(remainder_result2)

#keyword argument
remainder_result3 = remainder.remainder_by_value(45)
print(remainder_result3)

#varaible length argument
remainder_result4 = remainder.remainders_from_values(12, 34, 56, 23, 87, 26)
print(remainder_result4)

#keyword variable length argument
remainder_result5 = remainder.remainders_from_items(a=23, b=45, c=76)
print(remainder_result5)




