from examples.ExploreVariableLengthArgument import ExploreVariableLengthArgument

object = ExploreVariableLengthArgument()
input_values = ["hello", 559866, True, "hello guys", 198.23, "rama krishna", False, "ram = 20", 100.0,554795]
result = object.checking_variable_example(*input_values)
print(result)


object2 = ExploreVariableLengthArgument()
input_values = ["hello", 559866, True, "hello guys", 198.23, "rama raju", False, "ram = 20", 100.0,554795]
result = object2.checking_variable_values(*input_values)
print(result)


object3 = ExploreVariableLengthArgument()
input_values = ["hello", 547245, True, "hello guys", 198.23, "rama raju", False, "ram = 20", 100.0,554795]
result = object3.check_variables(*input_values)
print(result)


object4 = ExploreVariableLengthArgument()
input_values = ["hello", 559866, True, "hello guys", 198.23, "rama raju", False, "ram = 20", 100.0,554795]
result =object4.checking_arguments(*input_values)
print(result)