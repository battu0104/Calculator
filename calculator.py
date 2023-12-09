import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numerical values.")
        return

    operation = operation_var.get()

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Cannot divide by zero.")
            return
    else:
        messagebox.showerror("Error", "Invalid operation. Please choose a valid operation (+, -, *, /).")
        return

    result_label.config(text=f"Result: {result}")

# Create main window
window = tk.Tk()
window.title("Simple Calculator")

# Create entry widgets
entry_num1 = tk.Entry(window, width=15)
entry_num2 = tk.Entry(window, width=15)

# Create label widgets
result_label = tk.Label(window, text="Result: ")

# Create radio buttons for operations
operation_var = tk.StringVar()
operation_var.set('+')  # default operation
operations = ['+', '-', '*', '/']
operation_frame = tk.Frame(window)
for op in operations:
    tk.Radiobutton(operation_frame, text=op, variable=operation_var, value=op).pack(side=tk.LEFT)

# Create calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate)

# Place widgets in the window
entry_num1.pack(pady=10)
entry_num2.pack(pady=10)
operation_frame.pack(pady=10)
calculate_button.pack(pady=10)
result_label.pack(pady=10)

# Run the main loop
window.mainloop()
