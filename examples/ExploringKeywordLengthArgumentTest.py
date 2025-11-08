from ExploringKeywordLengthArgument import ExploringKeywordLengthArgument
#
# eObject = ExploringKeywordLengthArgument()  #Empty brackets because calling Default Constructor
# input_dictionary = {"name": "Rajesh", "city": "Hyderabad", "amount": 10000, "age" : 19, "class": 12, "section": "A", "Marks": 87.5, "fathername": "mohan rao", "mothername": "himabindhu", "Grandfather": "No"}
# result = eObject.checking_keyword_example(**input_dictionary)
# print(result)
#
# eObject2 = ExploringKeywordLengthArgument()
# input_dictionary = {"name": "Rahul", "city": "secendrabad", "amount": 80000, "age" : 26, "class":8, "section": "C", "Marks": 85.9, "fathername": "mahesh", "mothername": "Rupa", "grandfather": "yellaha"}
# result = eObject2.checking_keyword_example(**input_dictionary)
# print(result)
#
#
# eObject3 = ExploringKeywordLengthArgument()
# input_dictionary = {"name": "Ravi", "city": "kachiguda", "amount": 65330, "age" : 46, "class":14, "section": "p", "Marks": 764.54, "fathername": "Abilash", "mothername": "swapna", "grandfather": "parashuram"}
# result = eObject3.check_keyword(**input_dictionary)
# print(result)
#
#
#
# eObject4 = ExploringKeywordLengthArgument()
# input_dictionary = {"name": "johnny", "city": "jublihills", "amount": 56477, "age" : 76, "class":15, "section": "p", "Marks": 764.54, "fathername": "Abilash", "mothername": "swapna", "grandfather": "parashuram"}
# result = eObject4.checking_keyvalues(**input_dictionary)
# print(result)
#
# eObject5 = ExploringKeywordLengthArgument()
# input_dictionary = {"name": "prasad", "city": "himathnagar", "amount": 47561, "age" : 37, "class":16, "section": "p", "Marks": 764.54, "fathername": "Abilash", "mothername": "swapna", "grandfather": "parashuram"}
# print(type(input_dictionary))
# result = eObject5.checking_keyvalues(**input_dictionary)
# print(result)
#
#
#
# eObject6 = ExploringKeywordLengthArgument()
# input_dictionary = {"name": "prasad", "city": "himathnagar", "amount": 100.00, "age" : 37, "class":16, "section": "p", "Marks": 764.23, "fathername": "Abilash", "mothername": "swapna", "grandfather": "parashuram"}
# result = eObject6.checking_keyvalues(**input_dictionary)
# print(result)


eObject7 = ExploringKeywordLengthArgument()
input_dictionary = {"name": "vara prasad", "city": "himathnagar", "amount": 100.00, "cash" : 234.6, "age" : 37, "class" :16, "section": "A", "Marks": 764.23, "fathername": "Abilash", "mothername": "swapna", "grandfather": "parashuram"}
result = eObject7.checking_tyecasting(**input_dictionary)
print(result)





#isinstance(eObject,dict)
#Second Example
# eObject.checking_keyword_exmple(rollno=11,studnet_name="Suresh", school_name="St Xaviers High School")

"""
Expected Output:
{rollno:11, student_name = Suresh, school_name=St Xaviers High School}
"""

#appended_result = eObject.checking_keyword_appendHello(**input_dictionary)
"""
Expected output :
{amount : 10000Hello, name : krishnaHello, city : HyderabadHello }
"""
