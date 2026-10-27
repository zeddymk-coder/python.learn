print("Hello, World!")

#data transformation
prices_usd = [10, 20, 35, 50]
usd_to_tzs = 2500
prices_tzs = [price * usd_to_tzs for price in prices_usd]
print(prices_tzs)


#data extraction
customers = [
    {"name": "John", "age": 25},
    {"name": "Mary", "age": 30},
    {"name": "Peter", "age": 22},
]
customer_names = [customer["name"] for customer in customers]
print(customer_names)

products = [
    {"name": "Rice", "price":3000, "quantity": 10},
    {"name": "Sugar", "price":2500, "quantity": 5},
    {"name": "Beans", "price":4000, "quantity": 8}
]
products_names = [product["name"] for product in products]
print(products_names)


#data cleaning
customers = [
    "  john smith ",
    "MARRY JONES",
    "  peter brown  ",
    "aNNa WILSON"
]
customers = [name.strip().title() for name in customers]
print(customers)



#LEVEL 2

products = [
    {"name": "Rice", "unit_price": 3000, "quantity": 10},
    {"name": "Sugar", "unit_price": 2500, "quantity": 6},
    {"name": "Beans", "unit_price": 4000, "quantity": 8},
    {"name": "Cooking Oil", "unit_price": 6500, "quantity": 4}
]
total_inventory_value = sum(
    product["unit_price"] * product["quantity"] for product in products
)
for product in products:
    value = product["unit_price"] * product["quantity"]
    print(f"{product['name']}: {value}")

print(f"Total inventory value: {total_inventory_value}")


transactions = [
    {"customer": "John", "amount": 35000},
    {"customer": "Mary", "amount": 75000},
    {"customer": "Peter", "amount": 50000},
    {"customer": "Anna", "amount": 20000},
    {"customer": "James", "amount": 120000}
]

large_purchases = [
    transaction
    for transaction in transactions
    if transaction["amount"]>= 50000
]
print(large_purchases)


emails = [
    "  JOHN@gmail.com ",
    "mary@yahoo.com",
    "john@gmail.com",
    " PETER@gmail.com ",
    "MARY@yahoo.com ",
    "anna@gmail.com"
]

clean_email = [email.strip().lower() for email in emails]
unique_emails = list(dict.fromkeys(clean_email))
print(unique_emails)