from item import Item
from collections import deque
# Item(buy_price,fees,quantity,date)

class Item_manager():
    def __init__(self, id, name):
        self.inven = deque()
        self.sold_items = []
        self.count = 0
        self.id = id
        self.name = name
    
    def add_item(self, item:Item):
        if item.quantity > 0:
            self.count += item.quantity
            self.inven.append(item)

    def sell_item(self, sell_price, quantity, date):
        if self.count >= quantity:
            for item_to_be_sold in self.inven:
                
        else:
            print("Not enough inventory")
    

