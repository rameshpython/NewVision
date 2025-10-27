class StudentMarks :
    def __init__(self):
        pass
    def calculate(self):
        Marks = [80,75,85,65,85]
        #calculating total using sum()
        total = sum(Marks)
        #calculate average
        Average  = total/len(Marks)
        print("Marks of 5 subjects:",Marks)
        print("Total Marks:", total)
        print("Average Marks:", Average)


#Average Formula

#Average = sum of all values/number of values