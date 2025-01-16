print("PROFIT AND LOSS CALCULATOR \n --------------------------------------------")
buying_price = float(input("Enter the buying price: "))
selling_price = float(input("Enter the selling price: "))
print("--------------------------------------------------")

if selling_price > buying_price:
    print(f"Your profit is {selling_price - buying_price} shillings")
elif selling_price < buying_price:
    print(f"Your loss is {buying_price - selling_price} shillings")
elif selling_price == buying_price:
    print(f"no profit or loss")