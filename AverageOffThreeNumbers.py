class AverageOffThreeNumbers:
    def __init__(self):
        print("Object created successfully!")

    def average_off_three_numbers(self, number1, number2, number3):
        average = (number1 + number2 + number3) / 3
        print("The average of three numbers is:", average)


# Create object
demo = AverageOffThreeNumbers()

# Call method
demo.average_off_three_numbers(10, 20, 30)

