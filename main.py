from pyscript import document # type: ignore

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
    "Espresso": "P49",
    "Americano": "P79",
    "Vanilla Latte": "P99",
    "Macchiato": "P119",
    "Matcha Latte": "P179"
}

document.getElementById("restaurant_name").innerText = restaurant_name
document.getElementById("owner_name").innerText = f"Owner: {owner_name}"
document.getElementById("year_established").innerText = f"Since: {year_established}"
document.getElementById("operatingHours").innerText = f"Open: {open_time} - {close_time}"
document.getElementById("commonAllergens").innerText = f"May contain: {', '.join(common_allergens)}"

rows = ""
for item, price in menu_prices.items():
    rows = rows + f"<tr><td>{item}</td><td>{price}</td></tr>"

document.getElementById("product_names").innerHTML = rows
