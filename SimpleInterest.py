class SimpleInterest:
    def __init__(self):
        pass


    def calculate_interest(self,principal,time,rate):
            si = (principal * time * rate) / 100
            return si


d1 = SimpleInterest()

result=d1.calculate_interest(4564,2,4)
print("Simple Interest is result:",result)

result =d1.calculate_interest(7000,4,3)
print("Simple Interst is result:",result)













