import tkinter as tk

def on_click():
    label.config(text="Hello, " + entry.get())

root = tk.Tk()
root.title("Simple GUI")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Greet", command=on_click)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()
