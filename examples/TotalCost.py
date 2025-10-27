class TotalCost:
    def __init__(self):
        pass

    def get_data(self,quantity, price_per_item):
        self.quantity = quantity
        self.price_per_item = price_per_item

    def calculate_total(self):
        total = self.quantity * self.price_per_item
        return total




