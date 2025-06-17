import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def convert_temp():
    temp_type = temp_type_var.get()
    temp_input = temp_entry.get()

    try:
        temp_value = float(temp_input)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeric temperature.")
        return

    if temp_type == "Celsius":
        kelvin = temp_value + 273.15
        fahrenheit = (9/5) * temp_value + 32
        result_var.set(f"Kelvin: {round(kelvin, 2)} K\nFahrenheit: {round(fahrenheit, 2)} °F")

    elif temp_type == "Fahrenheit":
        kelvin = (temp_value - 32) * 5/9 + 273.15
        celsius = (temp_value - 32) * 5/9
        result_var.set(f"Kelvin: {round(kelvin, 2)} K\nCelsius: {round(celsius, 2)} °C")

    elif temp_type == "Kelvin":
        celsius = temp_value - 273.15
        fahrenheit = (temp_value - 273.15) * 9/5 + 32
        result_var.set(f"Celsius: {round(celsius, 2)} °C\nFahrenheit: {round(fahrenheit, 2)} °F")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("350x300")
root.resizable(False, False)

root.configure(bg="#f0f0f0")
font_label = ("Arial", 12)
font_result = ("Arial", 12, "bold")

tk.Label(root, text="Select Temperature Unit:", font=font_label, bg="#f0f0f0").pack(pady=10)
temp_type_var = tk.StringVar(value="Celsius")
temp_menu = ttk.Combobox(root, textvariable=temp_type_var, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly", width=20)
temp_menu.pack()

tk.Label(root, text="Enter Temperature Value:", font=font_label, bg="#f0f0f0").pack(pady=10)
temp_entry = tk.Entry(root, font=font_label, width=25)
temp_entry.pack()

convert_btn = tk.Button(root, text="Convert", command=convert_temp, font=font_label, bg="#4caf50", fg="white", width=15)
convert_btn.pack(pady=15)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=font_result, bg="#f0f0f0", justify="center")
result_label.pack(pady=10)

root.mainloop()