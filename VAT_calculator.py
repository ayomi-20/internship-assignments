# accepting sales amount from the user
sales_amount = float(input("Enter the product sales price: "))

# calculating the VAT based on the sales amount
_VAT = (18/100)*sales_amount

# calculating the total amount based on both the sales amount and the VAT
Total_amount = sales_amount + _VAT


print (f"for a given product sold at UGX {sales_amount},")
print (f"for which a standard VAT of 18% equivalent to UGX {_VAT} is charged,")
print(f"a customer would end up paying UGX {Total_amount} in total to purchase it")