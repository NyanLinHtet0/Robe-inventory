from item import Item

class inventory:
    def __init__(self):
        self.inven_data = {}
        
    def add_item(self, item:Item):
        iden1, iden2 = item.id[0:2],item.id[2:4]
        if iden1 not in self.inven_data:
            self.inven_data.update({iden1: {}})
            if iden2 not in self.inven_data[iden1]:
                self.inven_data[iden1].update({iden2:[[item],[]]})
        else:
            self.inven_data[iden1][iden2][0].append(item)
    
    def sell_item(self, id, price, quantity, date):
        iden1, iden2 = id[0:2],id[2:4]
        if iden1 in self.inven_data:
            if iden2 in self.inven_data[iden1]:
                self.inven_data[iden1][iden2].sell_item(price, quantity, date)
        else:
            print("Item not in inventory")

    def print(self):
        for item in self.inven_data['01']['01']:
            item.dislay()



# Example usage
item = Item("0101", "Malaysia", 300 , 30, 2, '01142024')
item = Item("0101", "Malaysia", 300 , 30, 2, '01152024')


inven = inventory()
inven.add_item(item)
inven.add_item(item)
inven.sell_item("0101",400, 2, "02142024")


inven.print()