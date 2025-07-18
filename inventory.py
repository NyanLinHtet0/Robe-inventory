from item import Item
from collections import deque

class inventory:
    def __init__(self):
        self.inven_data = {}
        
    def add_item(self, item:Item):
        iden1, iden2 = item.id[0:2],item.id[2:4]
        if iden1 not in self.inven_data:
            self.inven_data.update({iden1: {}})
        if iden2 not in self.inven_data[iden1]:
            self.inven_data[iden1].update({iden2:[deque(),[]]})
            self.inven_data[iden1][iden2][0].append(item)
        else:
            self.inven_data[iden1][iden2][0].append(item)

    
    def sell_item(self, id, price, quantity, date):
        iden1, iden2 = id[0:2],id[2:4]
        que_pop_count = 0
        sell_quant = quantity

        if self.inven_data[iden1][iden2][0]:
            for item_to_be_sold in self.inven_data[iden1][iden2][0]:

                if sell_quant == 0:
                    break

                avail_quantity = item_to_be_sold.quantity - item_to_be_sold.sold

                if sell_quant >= avail_quantity:
                    item_to_be_sold.sell_item(price, avail_quantity, date)
                    sell_quant -= avail_quantity
                    que_pop_count += 1
                else:
                    item_to_be_sold.sell_item(price, sell_quant, date)
                    sell_quant = 0
        else:
            print("Item not in inventory")
        

    def print(self):
        for iden1 in self.inven_data:
            for iden2 in self.inven_data[iden1]:
                for item in self.inven_data[iden1][iden2][0]:
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