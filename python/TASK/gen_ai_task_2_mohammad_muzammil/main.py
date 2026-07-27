
# TASK ONE (1)


# 1)

while True:
    try:
        order_amount = int(input("Enter order amount: "))
        break
    except ValueError:
        print("Please enter a numeric value.")

print("Order amount is:", order_amount)

if order_amount >= 2000:
    discount = (order_amount * 15) / 100

elif order_amount >= 1500:
    discount = (order_amount * 10) / 100

elif order_amount >= 1000:
    discount = (order_amount * 7) / 100

else:
    discount = 0

print("Discount:", discount)
print("Final Price:", order_amount - discount)

