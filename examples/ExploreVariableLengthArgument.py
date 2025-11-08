class ExploreVariableLengthArgument:
    def __init__(self):
        pass

    def checking_variable_example(self, *variable_arguments):
        result_list = []

        for value in variable_arguments:
            result_list.append(value)

        return  result_list




    def checking_variable_values(self, *variable_arguments):
        result_list = []

        for value in variable_arguments:
            if type(value) ==  str:
                result_list.append(value + "  hello")
        else:
            result_list.append(value)
        return result_list




    def check_variables(self,*variable_arguments):
        result_list = []

        for value in variable_arguments:
            if type(value) == int:
                result_list.append(str(value) + "  how are you")
            else:
                result_list.append(value)
        return result_list



    def checking_arguments(self,*variable_arguments):
        result_list =[]

        for value in variable_arguments:
            if type(value) == str:
                result_list.append(value + "  iam ramesh")
            elif type(value) == int:
                result_list.append(str(value) + " iam ramesh")
            elif type(value) == float:
                result_list.append(str(value) + "  iam ramesh")
            elif type(value) ==  bool:
                result_list.append(str(bool) + "  iam  ramesh")

            else:
                result_list.append(value)
        return result_list




def checking_arguments_vales(self, *variable_arguments):
    result_list = []

    for value in variable_arguments:
        if type(value) == str:
            result_list.append(value + "  iam ramesh")
        if type(value) == int:
            result_list.append(str(value) + " iam ramesh")
        if type(value) == float:
            result_list.append(str(value) + "  iam ramesh")
        if type(value) == bool:
            result_list.append(str(bool) + "  iam  ramesh")

        else:
            result_list.append(value)
    return result_list



