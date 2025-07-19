from item import Item
from collections import deque
from item_manager import Item_manager

class inventory:
    def __init__(self):
        self.inven_data = {}
        self.inven_data_all = {}

    def add_item(self, id, name, item:Item):
        iden1, iden2 = id[0:2], id[2:4]
        if iden1 not in self.inven_data:
            self.inven_data.update({iden1: {}})
        if iden2 not in self.inven_data[iden1]:
            self.inven_data[iden1].update({iden2:Item_manager(id, name)})
            self.inven_data[iden1][iden2].add_item(item)
        else:
            self.inven_data[iden1][iden2].add_item(item)

    
    def sell_item(self, id, price, quantity, date):
        iden1, iden2 = id[0:2],id[2:4]

        if self.inven_data[iden1][iden2]:
            self.inven_data[iden1][iden2].sell_item(price, quantity, date)
        else:
            print("Item not in inventory")
        

    def print(self):
        for iden1 in self.inven_data:
            for iden2 in self.inven_data[iden1]:
                for item in self.inven_data[iden1][iden2].inven:
                    item.display()
                    print()



# # # Example usage
# item = Item("0101", "Malaysia", 300 , 30, 2, '01/14/2024')
# item2 = Item("0101", "Malaysia", 500 , 50, 2, '01/15/2024')


# inven = inventory()
# inven.add_item(item)
# inven.add_item(item2)
# inven.sell_item("0101",400, 3, "02/14/2024")


# inven.print()