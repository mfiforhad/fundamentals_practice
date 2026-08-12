"""
Write code to:
-> Calculate total quantity of every product across all warehouses.
-> Find the warehouse with the highest total inventory.
-> Find products that exist in every warehouse.
-> Find products that exist in only one warehouse.
-> Find the category with the highest total quantity.

Create:
{
    "laptop": {
        "Dhaka": 15,
        "Chittagong": 8
    },
    ...
}
Important: Don't manually access "Dhaka" and "Chittagong". Your code should work if another warehouse is added.
"""


inventory = {
    "Dhaka": {
        "electronics": {"laptop": 15, "phone": 30, "tablet": 10},
        "furniture": {"chair": 50, "desk": 20},
    },
    "Chittagong": {
        "electronics": {"laptop": 8, "phone": 20, "tablet": 5},
        "furniture": {"chair": 30, "desk": 10},
    },
}

# total quantity of every product across all warehouses
total_product_quantity = {}
warehouse_total_inventory = {}
warehouse_products = {}
category_total = {}

for warehouse, product_category in inventory.items():
    # print(warehouse, product_category)
    warehouse_total_inventory.setdefault(warehouse, 0)
    warehouse_products.setdefault(warehouse, set())
    for products in product_category.values():
        # print(value)
        for product, qty in products.items():
            total_product_quantity.setdefault(product, {}).setdefault(warehouse, 0)
            total_product_quantity[product][warehouse] += qty
            warehouse_total_inventory[warehouse] += qty
            warehouse_products[warehouse].add(product)
            category_total.setdefault(product, 0)
            category_total[product] += qty


print(f"total_product_quantity: {total_product_quantity}")
print(f"warehouse_total_inventory: {warehouse_total_inventory}")
print(f"warehouse_products: {warehouse_products}")
print(f"category_total: {category_total}")

# Find the warehouse with the highest total inventory.

top_warehouse = max(
    warehouse_total_inventory, key=lambda x: warehouse_total_inventory[x]
)

print(f"top warehouse: {top_warehouse}")

# Find products that exist in every warehouse.
warehouse_1, warehouse_2 = warehouse_products.values()
stock_everywhere = warehouse_1 & warehouse_2
print(f"stock_everywhere: {stock_everywhere}")

# Find products that exist in only one warehouse.
stock_in_one_warehouse = warehouse_1 ^ warehouse_2

# Find the category with the highest total quantity.
highest_stock = max(category_total, key=lambda x: category_total[x])
print(f"highest_stock: {highest_stock}")
