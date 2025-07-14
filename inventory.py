from item import Item

class inventory:
    def __init__(self):
        self.inven_data = {}
        
    def add_item(self, item:Item):
        iden1, iden2 = item.id[0:2],item.id[2:4]
        if iden1 not in self.inven_data:
            self.inven_data.update({iden1: {}})
            if iden2 not in self.inven_data[iden1]:
                self.inven_data[iden1].update({iden2:[item]})
        else:
            self.inven_data[iden1][iden2].append(item)
            
        
        
    def print(self):
        print(self.inven_data['01']['01'])



# Example usage
item = Item("0101", "Malaysia", 300 , 30, 2, '01142024')

inven = inventory()
inven.add_item(item)
inven.add_item(item)


inven.print()