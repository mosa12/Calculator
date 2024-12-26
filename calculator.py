import tkinter as tk
from tkinter import messagebox

# Function to handle button click
def on_button_click(value):
    if value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Expression")
    elif value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

# Create the main window
root = tk.Tk()
root.title("Desktop Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Create the entry field
entry = tk.Entry(root, font=("Arial", 20), borderwidth=2, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Add buttons to the window
for i, button_text in enumerate(buttons):
    row = (i // 4) + 1
    col = i % 4
    button = tk.Button(
        root, text=button_text, font=("Arial", 18), width=5, height=2,
        command=lambda value=button_text: on_button_click(value)
    )
    button.grid(row=row, column=col, padx=5, pady=5)

# Start the main loop
root.mainloop()
