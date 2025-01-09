class Product:
    ID = 0
    name = "name"
    qty = 0


products = Product()
products.name = ["shampoo", "conditioner", "detergent"]
products.ID = [101, 102, 103]
products.qty = [38, 20, 54]

for name, ID, qty in zip(products.name, products.ID, products.qty):
    print(f"Product name: {name}")
    print(f"Product ID: {ID}")
    print(f"Product Qty: {qty}")
    print(f"{' ':-<20}")
