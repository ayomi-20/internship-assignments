# empty products list 
products = []

# an empty dictionary storing inventory
inventory = {}

# input methods for product name and quantity
product = input("Enter product name: ")
quantity = int(input("Enter quantity: "))

# methods that add a user added product to theproduct list and inventory 
products.append(product)
inventory[product] = quantity

# print statements
print("\nProducts:", products)
print("Inventory:", inventory)