class ExploringKeywordLengthArgument:
    def __init__(self):  # Empty constructor
        pass

    def checking_keyword_example(self, **keyword_arguments):
        dictionary = {}

        for key, value in keyword_arguments.items():
            if type(value) == str:
                dictionary[key] = value +  " Hii"
            else:
                dictionary[key] = value
        return dictionary



    def check_keyword(self, **keyword_arguments):
        dictionary = {}

        for key, value in keyword_arguments.items():
            if type(value) == int:
                dictionary[key] = str(value) + " Hello"
            else:
                dictionary[key] = value
        return dictionary



    def checking_keyvalues(self, **keyword_arguments):
        dictionary ={}

        for key, value in keyword_arguments.items():
            if type(value) != int:
                dictionary[key] = str(value) + " Ramesh babu"
            elif type(value) == str:
                    dictionary[key] = value + "Ramesh bahai"

            else:
                dictionary[key] = value
        return dictionary




    def checking_keyvalues(self, **keyword_arguments):
        dictionary = {}

        for key, value in keyword_arguments.items():
            if type(value) == int:
                dictionary[key] = str(value) + " jai bolo ganesh"
            elif type(value) == str:
                    dictionary[key] = value + " jai bolo ganesh"

            else:
                dictionary[key] = value
        return dictionary






    def check_key_value_types(self, **keyword_arguments):
        dictionary = {}

        for key, value in keyword_arguments.items():
            if type(value) == int:
                dictionary[key] = str(value) + str(type(value))
            elif type(value) == str:
                dictionary[key] = value + str(type(value))
            elif type(value) == float:
                dictionary[key] = str(value) + str(type(value))
            else:
                dictionary[key] = value

        return dictionary






    def checking_tyecasting(self, **keyword_arguments):
        dictionary = {}

        for key, value in keyword_arguments.items():
            if type(value) == int:
                dictionary[key] = str(value) + str(type(value))
            elif type(value) == str:
                dictionary[key] = value + " : String Datatype"
            elif type(value) == float:
                dictionary[key] = format(value, ".6f") +": Float Datatype"
            else:
                dictionary[key] = value

        return dictionary







#        dictionary["name"] = "rakesh"
#        dictionary["city"] = "hyderabad"
#        dictionary["amount"] = "5000"

#    def checking_keyword_appendHello(self, **keyword_arguments):
#        dictonary = {}
