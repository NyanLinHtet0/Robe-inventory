class Item:
    def __init__(self, id, name, price, fees, quantity, date):
        self.id = id #unique identifier
        self.name = name
        self.price = price
        self.fees = fees
        self.quantity = quantity
        self.date = date
        self.sold = 0
        self.sell_list = []

        
    def get_cost_per_item(self):
        return (self.price+self.fees)
    
    def get_total_cost(self):
        return self.get_cost_per_item()*self.quantity

    def display(self):
        print(f"{self.name}: ${self.price:.2f} x {self.quantity} = ${self.total_cost():.2f}")
        
    def display(self):
        print(f"Item ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Fees: ${self.fees:.2f}")
        print(f"Quantity: {self.quantity}")
        print(f"Cost per item (with fees): ${self.get_cost_per_item():.2f}")
        print(f"Total cost: ${self.get_total_cost():.2f}")

