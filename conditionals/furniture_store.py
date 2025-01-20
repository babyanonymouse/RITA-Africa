# Breakout Session
# TASK: You have a furniture store.Create an invoice for your client,
# giving them a price discount and a final price for their order depending on their membership category.
# Bronze: 5 %, Silver: 10 %, Gold: 15 % and Platinum: 20 %

print(" --- THE FURNITURE STORE CASHIER 1 --- ")
# dictionary and keys
discount_rates = {
    "bronze": .05,
    "silver": .1,
    "gold": .15,
    "platinum": .2
}

client_name = str(input("Enter name: "))
membership = str(input("Enter the membership (bronze, gold, silver, platinum): ").lower())
furniture_item = str(input("Enter the item name: "))
order_total = float(input("Enter order total: "))

# validate membership
if membership in discount_rates:
    discount_rate = discount_rates[membership]
    discount = order_total * discount_rate
    final_price = order_total - discount
else:
    print("invalid membership category")
    exit()

#     invoice
print(" --- Furniture Store invoice --- ")
print(f"Client Name: {client_name.capitalize()}")
print(f"Membership: {membership.capitalize()}")
print(f"Item Name: {furniture_item}")
print(f"Order Total: ${order_total:.2f}")
print(f"Discount: ({int(discount_rate * 100)}%): -${discount:.2f}")
print(f"Final Price: ${final_price:.2f}")
print("-------------------------------------")
