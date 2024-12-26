import tkinter as tk
from tkinter import messagebox

# Function to handle button click
def on_button_click(value):
    if value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
    elif value == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, value)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")
root.resizable(False, False)
root.configure(bg="#2C3E50")

# Create the entry field
entry = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="flat", justify="right", bg="#ECF0F1", fg="#2C3E50")
entry.grid(row=0, column=0, columnspan=4, padx=15, pady=20, ipady=10)

# Button styles
button_style = {
    "font": ("Arial", 18),
    "width": 5,
    "height": 2,
    "bg": "#34495E",
    "fg": "#ECF0F1",
    "activebackground": "#1ABC9C",
    "activeforeground": "#ECF0F1",
    "relief": "flat"
}

# Button layout
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
        root, text=button_text, command=lambda value=button_text: on_button_click(value), **button_style
    )
    button.grid(row=row, column=col, padx=10, pady=10)

# Highlight special buttons
special_buttons = {"=": "#1ABC9C", "C": "#E74C3C"}
for button_text, color in special_buttons.items():
    button = root.grid_slaves(row=(buttons.index(button_text) // 4) + 1, column=buttons.index(button_text) % 4)[0]
    button.configure(bg=color, fg="#FFFFFF")

# Start the main loop
root.mainloop()
