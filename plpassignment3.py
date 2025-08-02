def calculate_discount(price ,discount_percent):
    result=price*discount_percent
    if discount_percent >= 0.2:
        return result
    else:
        return price
    
price_input=float(input("Enter the original price of the item:"))
discount_input=float(input("Enter the discount percentage:"))
final_price=calculate_discount(price_input , discount_input)
print("final price after the discount:", final_price)