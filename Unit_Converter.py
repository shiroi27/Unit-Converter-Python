import tkinter as tk
from tkinter import ttk

# Conversion logic
def convert():
    try:
        value = float(entry.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()

        conversion_factors = {
            "Kilometers": 1000,
            "Meters": 1,
            "Centimeters": 0.01,
            "Millimeters": 0.001,
            "Miles": 1609.34,
            "Yards": 0.9144,
            "Feet": 0.3048,
            "Inches": 0.0254
        }

        if from_unit in conversion_factors and to_unit in conversion_factors:
            meters = value * conversion_factors[from_unit]
            result = meters / conversion_factors[to_unit]
            result_label.config(text=f"{value} {from_unit} = {round(result, 4)} {to_unit}")
        else:
            result_label.config(text="Invalid unit selection.")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# UI Setup
root = tk.Tk()
root.title("Unit Converter")
root.geometry("500x380+500+250")
root.config(bg="#52B3EB")
root.resizable(False, False)

# Header
header = tk.Label(root, text="📏 UNIT CONVERTER", font=("Times New Roman", 24, "bold"), bg="#FFE851", fg="#000000")
header.pack(fill="x")

# Decorative Line
tk.Frame(root, height=6, bg="#6EFFFF").pack(fill="x")

# Input
frame = tk.Frame(root, bg="#52B3EB")
frame.pack(pady=30)

tk.Label(frame, text="Enter value:", font=("Times New Roman", 14), bg="#52B3EB", fg="#000000").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(frame, font=("Times New Roman", 14), width=12)
entry.grid(row=0, column=1)

tk.Label(frame, text="From:", font=("Times New Roman", 14), bg="#52B3EB", fg="#000000").grid(row=1, column=0, padx=10)
combo_from = ttk.Combobox(frame, values=["Kilometers", "Meters", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"], font=("Times New Roman", 12))
combo_from.grid(row=1, column=1)
combo_from.set("Meters")

tk.Label(frame, text="To:", font=("Times New Roman", 14), bg="#52B3EB", fg="#000000").grid(row=2, column=0, padx=10)
combo_to = ttk.Combobox(frame, values=["Kilometers", "Meters", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"], font=("Times New Roman", 12))
combo_to.grid(row=2, column=1)
combo_to.set("Kilometers")

# Convert button
tk.Button(root, text="CONVERT", font=("Times New Roman", 14, "bold"), bg="#9BA4B5", fg="#000000", command=convert).pack(pady=10)

# Output Display Box
output_box_frame = tk.Frame(root, bg="#FFFFFF", bd=3, relief="solid", width=320, height=40)
output_box_frame.place(x=90, y=295)

# Output Label
result_label = tk.Label(root, text="", font=("Times New Roman", 14, "bold"), bg="#FFFFFF", fg="#000000")
result_label.place(x=95, y=300)

# Footer
footer = tk.Label(root, text="Made with ❤️ using Python & Tkinter", font=("Times New Roman", 10, "italic"), bg="#52B3EB", fg="#000000")
footer.pack(side="bottom", pady=8)

root.mainloop()