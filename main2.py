import tkinter as tk
from tkinter import ttk

from item import Item
from inventory import inventory
from item_manager import Item_manager
inven = inventory()
item = Item(300 , 30, 2, '01/14/2024')
item2 = Item(500 , 50, 2, '01/15/2024')
inven.add_item("0101", "Malaysia", item)
inven.add_item("0101", "Malaysia",item2)

root = tk.Tk()
root.title("Greeting App")
root.geometry("1000x800")
# Configure 2 columns to share space equally
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=5)

# # Optional: Make rows flexible too
# root.grid_rowconfigure(0, weight=1)
# root.grid_rowconfigure(1, weight=1)

tree = ttk.Treeview(root)
tree_constants = {
    "01":"Thin Gan",
    "02":"Shoe",
    "03":"Tha Bate"
}

def on_tree_select(event):
    selected_id = tree.focus()  # ID of the selected node
    item_text = tree.item(selected_id, "text")
    print("Selected ID:", selected_id)
    print("Selected Text:", item_text)

    # Example: check if it's a top-level branch
    if tree.parent(selected_id) == "":
        print("This is a top-level branch!")
    else:
        print("This is a child node.")
    
# Add top-level items
for iden1 in tree_constants:
    branch_name=tree_constants[iden1]
    parent_id =tree.insert("","end", text = branch_name)
    if iden1 in inven.inven_data:
        for iden2 in inven.inven_data[iden1]:
            tree.insert(parent_id,"end", text = inven.inven_data[iden1][iden2].name)
            
         
tree.bind("<<TreeviewSelect>>", on_tree_select)

        
# inventory_id = tree.insert("", "end", text="Inventory")


tree.grid(column=0, sticky="nsew")

root.mainloop()