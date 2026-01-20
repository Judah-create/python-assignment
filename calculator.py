import tkinter as tk

def add():
    a = int(entry1.get())
    b = int(entry2.get())
    result.config(text="Result: " + str(a + b))

def subtract():
    a = int(entry1.get())
    b = int(entry2.get())
    result.config(text="Result: " + str(a - b))

def multiply():
    a = int(entry1.get())
    b = int(entry2.get())
    result.config(text="Result: " + str(a * b))

def divide():
    a = int(entry1.get())
    b = int(entry2.get())
    result.config(text="Result: " + str(a / b))

window = tk.Tk()
window.title("Calculator")

entry1 = tk.Entry(window)
entry1.pack()

entry2 = tk.Entry(window)
entry2.pack()

tk.Button(window, text="Add", command=add).pack()
tk.Button(window, text="Subtract", command=subtract).pack()
tk.Button(window, text="Multiply", command=multiply).pack()
tk.Button(window, text="Divide", command=divide).pack()

result = tk.Label(window, text="Result:")
result.pack()

window.mainloop()
