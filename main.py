from pyscript import display, document # type: ignore

restaurant_name = "Brew, Brew, Brew Your Float" #string

owner_name = "Caleb Matig-a" #string

year_established = "2010" #string

business_hours = ("11:00 AM", "9:00 PM") #tuple

open_time, close_time = business_hours #all string

popular_item_price = 179 #integer

has_delivery = False #boolean

common_allergens = ["Dairy", "Histamine","Caffeine","Vanilla"] #list

tax_rate = 0.1 #floating-point

product_names = [ #list
    "Espresso",
    "Americano", 
    "Vanilla Latte", 
    "Macchiato", 
    "Matcha Latte"
    ]

menu_prices = { #dict
    "Espresso": 49,
    "Americano": 79,
    "Vanilla Latte": 99,
    "Macchiato": 119,
    "Matcha Latte": 179
}

display(restaurant_name, target="restaurant_name")
display(f"Owner: {owner_name}", target="owner_name")
display(f"Since {year_established}", target="year_established")
display(f"Is Delivery Available In Your Area?:", target="question")
display(has_delivery, target="delivery")
document.getElementById("operatingHours").innerText = f"Open: {open_time} - {close_time}"
document.getElementById("commonAllergens").innerText = f"May contain: {', '.join(common_allergens)}"

# Display menu items
display(product_names[0], target="prod1")
display(f"₱{menu_prices['Espresso']:.2f}", target="price1")
display(product_names[1], target="prod2")
display(f"₱{menu_prices['Americano']:.2f}", target="price2")
display(product_names[2], target="prod3")
display(f"₱{menu_prices['Vanilla Latte']:.2f}", target="price3")
display(product_names[3], target="prod4")
display(f"₱{menu_prices['Macchiato']:.2f}", target="price4")
display(product_names[4], target="prod5")
display(f"₱{menu_prices['Matcha Latte']:.2f}", target="price5")