



product = ["phon","laptop","computer","chair","table","keyboard"]
sample_product = ("phon","smart",20000)





# second product
print(product[1])
# last product
print(product[-1])


# appending
product.append("tablet")
product.append("charger")

print(product)


# changing into tuple to list
updated_tuple =list(sample_product)
updated_tuple[-1] = 25000
sample_product =tuple(updated_tuple)

print(sample_product)


# Task Two

# create new list for categories

categories = [
    "Electronics",
    "Accessories",
    "Accessories",
    "Electronics",
    "Electronics",
    "Electronics"
]

# converting that into set data type 
categories_set = set(categories)
categories_set.add("Naturally")

# print that categories exist or not
print("Electronics" in categories_set)

# totle number of unique number
print(len(categories_set))


# TASK THREE (3)


# creating dictionary 

price_dict = { "mobile":15000 ,"laptop":60000 , "table":2000 , "tablet":30000 , "chair":2000, "charger":1000}

# add new item
price_dict["printer"] = 20000

# update item
price_dict["table"] = 25000

# delete item

del price_dict["mobile"]

# handling if item not exist
if "Camera" in price_dict:
    del price_dict["Camera"]
else:
    print("Product not found")

    total = sum(price_dict.values())

# Total products
count = len(price_dict)

# Average price
average = total / count

print("Average Price:", average)



# TASK Four

products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Phone", "Tablet"]

categories = [
    "Electronics",
    "Accessories",
    "Accessories",
    "Electronics",
    "Electronics",
    "Electronics"
]

price_dict = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1200,
    "Monitor": 10000,
    "Phone": 25000,
    "Tablet": 18000
}

# Step 1: Catalog banana
catalog = []

for i in range(len(products)):
    catalog.append((products[i], price_dict[products[i]], categories[i]))

print("Catalog:")
print(catalog)

category_to_products = {}

for i in range(len(products)):

    category = categories[i]
    product = products[i]

    if category not in category_to_products:
        category_to_products[category] = []

    category_to_products[category].append(product)

print(category_to_products)

print("Products in Electronics:")

for product in category_to_products["Electronics"]:
    print(product)