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
inven.add_item("0102", "Singapore",item2)
inven.add_item("0103", "Singaporezzzzzzzzzzzzzzzzzz",item2)
inven.add_item("0104", "CYC",item2)



root = tk.Tk()
style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 14))   # Header font
style.configure("Treeview", font=("Arial", 12))           # Cell font



# Display box on the right
display_frame = tk.Frame(root, relief="groove", borderwidth=2, padx=0, pady=0)
display_frame.grid(row=0, column=1, sticky="nsew", padx=0, pady=0)



root.title("Greeting App")
root.geometry("1000x800")
# Configure 2 columns to share space respectfully
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=6)

tree = ttk.Treeview(root)
tree_constants_l1 = {
    "01":"Thin Gan",
    "02":"Shoe",
    "03":"Tha Bate"
}
tree_constants_l2 = {
    "0101":"Thin Gan",
    "01":"Shoe",
    "03":"Tha Bate"
}

def on_tree_select(event, display_frame):
    selected_item = tree.selection()[0]
    if selected_item in tree_object_map:
        obj = tree_object_map[selected_item]
        print("Selected object:", obj)

        # Optional: Display in display_frame
        for widget in display_frame.winfo_children():
            widget.destroy()

        tk.Label(
            display_frame,
            text=obj.get_report_string(),
            anchor="w",
            font=("Arial", 30),
            # text inside widget is left-aligned
            justify="left"      # for multi-line text
        ).grid(row=0, column=0, sticky="w")



tree_object_map = {}  # Maps treeview item IDs to actual objects

# inventory_id = tree.insert("", "end", text="Inventory")
tree.grid(row=0,column=0, sticky="nsew")
# Add top-level items
for iden1 in tree_constants_l1:
    branch_name = tree_constants_l1[iden1]
    parent_id = tree.insert("", "end", text=branch_name)
    
    if iden1 in inven.inven_data:
        for iden2 in inven.inven_data[iden1]:
            obj = inven.inven_data[iden1][iden2]  # Your actual object
            child_id = tree.insert(parent_id, "end", text=obj.name)
            tree_object_map[child_id] = obj  # Store the reference


         
tree.bind("<<TreeviewSelect>>", lambda event: on_tree_select(event, display_frame))


        





root.mainloop()