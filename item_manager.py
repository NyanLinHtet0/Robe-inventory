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
            sell_quant = quantity
            for item_to_be_sold in self.inven:
                if sell_quant == 0:
                    break
                avail_quantity = item_to_be_sold.quantity - item_to_be_sold.sold
                if sell_quant >= avail_quantity:
                    item_to_be_sold.sell_item(sell_price, avail_quantity, date)
                    sell_quant -= avail_quantity
                else:
                    item_to_be_sold.sell_item(sell_price, sell_quant, date)
                    sell_quant = 0  
        else:
            print("Not enough inventory")

    def get_report_string(self):
        string_result = f'ID: {self.id}\nName: {self.name}\nInventory: {self.count}'
        print(string_result)
        return string_result
    

