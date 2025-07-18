class Item:
    def __init__(self, price, fees, quantity, date):
        self.price = price
        self.fees = fees
        self.quantity = quantity
        self.date = date
        self.sold = 0
        self.sell_list = []

    def sell_item(self, price, quantity, date):
        if self.quantity >= (self.sold + quantity):
            self.sold += quantity
            self.sell_list.append((quantity,price,date))
            if self.quantity == (self.sold):
                self.sold = -1
            return True
        else:
            #unable to sell item, insuffecient stock
            pass
        
    def get_cost_per_item(self):
        return (self.price+self.fees)
    
    def get_total_cost(self):
        return self.get_cost_per_item()*self.quantity

    def display(self):
        print(f"{self.name}: ${self.price:.2f} x {self.quantity} = ${self.total_cost():.2f}")
        
    def display(self):
        print(f"Date: {self.date}")
        print(f"Item info:({self.quantity} x {(self.price+self.fees):.2f} ({self.price}+ {self.fees})")
        print(f"Total cost: {self.get_total_cost():.2f}")
        print(f"Total Sold: {self.sold}")
        if self.sold == -1:
            for item in self.sell_list:
                print(f"Quantity: {item[0]}, Price: {item[1]}, Date: {item[2]}")

