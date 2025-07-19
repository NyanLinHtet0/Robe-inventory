from item import Item
from item_manager import Item_manager

class Warehouse_manager:
    def __init__(self):
        self.data = {}
    
    def add_item(self, id, name, item:Item):
        id1,id2 = id[0:2],id[2:4]
        if id1 in self.data:
            self.data[id1].add_item(item)
        else:
            self.data[id1] = Item_manager(id, name)
            self.data[id1].add_item(item)
    
    def sell_item(self, id, price, quantity, date):
        id1,id2 = id[0:2],id[2:4]
        if id1 in self.data:
            self.data[id1].sell_item(price,quantity,date)

