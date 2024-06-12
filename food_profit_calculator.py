import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def calculate_profit():
    try:
        # Input values
        number_of_omelettes = int(entry_quantity_omelettes.get())
        number_of_waffles = int(entry_quantity_waffles.get())
        number_of_cappuccinos = int(entry_quantity_cappuccinos.get())
        number_of_orange_juice = int(entry_quantity_orange_juice.get())
        
        if number_of_omelettes > 1_000_000 or number_of_cappuccinos > 1_000_000 or number_of_orange_juice > 1_000_000 or number_of_waffles > 1_000_000:
            messagebox.showerror("Input Error", "The number of orders cannot exceed 1,000,000.")
            return
        
        # Ingredient costs and quantities for omelettes
        eggs_cost = 4.00
        onions_cost = 1.99
        carrots_cost = 3.99
        cheese_cost = 3.99
        chile_cost = 1.99
        
        eggs_quantity = 12
        onions_quantity = 16
        carrots_quantity = 14
        cheese_quantity = 10
        chile_quantity = 16
        
        # Calculate total cost of ingredients per omelette
        cost_per_omelette = (
            (eggs_cost / eggs_quantity) +
            (onions_cost / onions_quantity) +
            (carrots_cost / carrots_quantity) +
            (cheese_cost / cheese_quantity) +
            (chile_cost / chile_quantity)
        )
        
        # Costs and prices for other items
        cost_per_cappuccino = 0.70
        selling_price_cappuccino = 4.00
        
        cost_per_orange_juice = 2 * 0.99
        selling_price_orange_juice = 5.00
        
        cost_per_waffle_mix = 3.99 / 12 * 2  # Cost for 2 waffles
        selling_price_waffle = 10.00
        
        # Calculate total cost, revenue (gross proceeds), gross profit, and net profit for all items
        total_cost_omelettes = cost_per_omelette * number_of_omelettes
        total_revenue_omelettes = 10 * number_of_omelettes

        total_cost_waffles = cost_per_waffle_mix * number_of_waffles
        total_revenue_waffles = selling_price_waffle * number_of_waffles
        
        total_cost_cappuccinos = cost_per_cappuccino * number_of_cappuccinos
        total_revenue_cappuccinos = selling_price_cappuccino * number_of_cappuccinos
        
        total_cost_orange_juice = cost_per_orange_juice * number_of_orange_juice
        total_revenue_orange_juice = selling_price_orange_juice * number_of_orange_juice
        
        total_cost = total_cost_omelettes + total_cost_orange_juice + total_cost_waffles + total_cost_cappuccinos
        total_revenue = total_revenue_omelettes + total_revenue_waffles + total_revenue_cappuccinos + total_revenue_orange_juice
        gross_profit = total_revenue - total_cost
        net_profit = gross_profit * (1 - 0.3)  # Total net profit
        
        label_total_cost_value.config(text=f"${total_cost:.2f}")
        label_revenue_value.config(text=f"${total_revenue:.2f}")
        label_gross_profit_value.config(text=f"${gross_profit:.2f}")
        label_net_profit_value.config(text=f"${net_profit:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for the quantities.")

# Create the main window
root = tk.Tk()
root.title("Food Profit Calculator")

# Color scheme
background_color = "#010111"  # dark blue
foreground_color = "#ffffff"  # white for text

# Set the background color
root.configure(bg=background_color)

# Add the logo
logo_path = "/Users/prickie/Desktop/MultiAgents/Stanford/logo2.png"
logo_image = Image.open(logo_path)
logo_image = logo_image.resize((150, 150), Image.Resampling.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

logo_label = tk.Label(root, image=logo_photo, bg=background_color)
logo_label.grid(row=0, column=0, columnspan=2, pady=10)

# Title
title_label2 = tk.Label(root, text="Welcome to\n Order Profit Calculator", font=('Helvetica', 24,), bg=background_color, fg=foreground_color)
title_label2.grid(row=2, column=0, columnspan=2, pady=5)

# Subheading
subheading_label = tk.Label(root, text="Enter the number of orders\n you would like to calculate:", font=('Helvetica', 16), bg=background_color, fg=foreground_color, anchor="center")
subheading_label.grid(row=3, column=0, columnspan=2, pady=10, sticky="n")

# Create and place the widgets with the color scheme
label_quantity_omelettes = tk.Label(root, text="Omelettes:", bg=background_color, fg=foreground_color, anchor="w")
label_quantity_omelettes.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_quantity_omelettes = tk.Entry(root, width=15)
entry_quantity_omelettes.grid(row=4, column=1, padx=10, pady=5, sticky="e")

label_quantity_waffles = tk.Label(root, text="Waffles (orders of 2):", bg=background_color, fg=foreground_color, anchor="w")
label_quantity_waffles.grid(row=5, column=0, padx=10, pady=5, sticky="w")
entry_quantity_waffles = tk.Entry(root, width=15)
entry_quantity_waffles.grid(row=5, column=1, padx=10, pady=5, sticky="e")

label_quantity_cappuccinos = tk.Label(root, text="Cappuccinos:", bg=background_color, fg=foreground_color, anchor="w")
label_quantity_cappuccinos.grid(row=6, column=0, padx=10, pady=5, sticky="w")
entry_quantity_cappuccinos = tk.Entry(root, width=15)
entry_quantity_cappuccinos.grid(row=6, column=1, padx=10, pady=5, sticky="e")

label_quantity_orange_juice = tk.Label(root, text="Fresh Orange Juice:", bg=background_color, fg=foreground_color, anchor="w")
label_quantity_orange_juice.grid(row=7, column=0, padx=10, pady=5, sticky="w")
entry_quantity_orange_juice = tk.Entry(root, width=15)
entry_quantity_orange_juice.grid(row=7, column=1, padx=10, pady=5, sticky="e")

button_calculate = tk.Button(root, text="Calculate Profit", command=calculate_profit, bg=foreground_color, fg=background_color)
button_calculate.grid(row=8, column=0, columnspan=2, pady=20)

# Result labels
label_total_cost = tk.Label(root, text="Total cost:", bg=background_color, fg=foreground_color, anchor="w")
label_total_cost.grid(row=9, column=0, padx=10, pady=5, sticky="w")
label_total_cost_value = tk.Label(root, text="", bg=background_color, fg=foreground_color, anchor="e")
label_total_cost_value.grid(row=9, column=1, padx=10, pady=5, sticky="e")

label_revenue = tk.Label(root, text="Gross proceeds (revenue):", bg=background_color, fg=foreground_color, anchor="w")
label_revenue.grid(row=10, column=0, padx=10, pady=5, sticky="w")
label_revenue_value = tk.Label(root, text="", bg=background_color, fg=foreground_color, anchor="e")
label_revenue_value.grid(row=10, column=1, padx=10, pady=5, sticky="e")

label_gross_profit = tk.Label(root, text="Gross profit:", bg=background_color, fg=foreground_color, anchor="w")
label_gross_profit.grid(row=11, column=0, padx=10, pady=5, sticky="w")
label_gross_profit_value = tk.Label(root, text="", bg=background_color, fg=foreground_color, anchor="e")
label_gross_profit_value.grid(row=11, column=1, padx=10, pady=5, sticky="e")

label_net_profit = tk.Label(root, text="Total net profit:", bg=background_color, fg=foreground_color, anchor="w", font=('Helvetica', 16, 'bold'))
label_net_profit.grid(row=12, column=0, padx=10, pady=5, sticky="w")
label_net_profit_value = tk.Label(root, text="", bg=background_color, fg=foreground_color, anchor="e", font=('Helvetica', 16, 'bold'))
label_net_profit_value.grid(row=12, column=1, padx=10, pady=5, sticky="e")
                        
# Add padding for bottom space
bottom_padding = tk.Label(root, text="", bg=background_color)
bottom_padding.grid(row=12, column=0, columnspan=2, pady=10)

# Start the main event loop
root.mainloop()