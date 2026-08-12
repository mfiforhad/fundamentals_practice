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
from collections import defaultdict

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

def analyze_inventory(inventory):
    product_quantities = defaultdict(dict)
    warehouse_totals = defaultdict(int)
    warehouse_products = defaultdict(set)
    category_totals = defaultdict(int)

    for warehouse, categories in inventory.items():
        for category, products in categories.items():
            for product, quantity in products.items():
                product_quantities[product][warehouse] = quantity
                warehouse_totals[warehouse] += quantity
                warehouse_products[warehouse].add(product)
                category_totals[category] += quantity

    product_warehouse_count = defaultdict(int)

    for products in warehouse_products.values():
        for product in products:
            product_warehouse_count[product] += 1

    return {
        "product_quantities": dict(product_quantities),
        "warehouse_totals": dict(warehouse_totals),
        "top_warehouse": max(warehouse_totals, key=lambda x: warehouse_totals[x]),
        "stock_everywhere": set.intersection(*warehouse_products.values()),
        "stock_in_one_warehouse": {
            product for product, count in product_warehouse_count.items() if count == 1
        },
        "category_totals": dict(category_totals),
        "top_category": max(category_totals, key=lambda x: category_totals[x]),
    }


result = analyze_inventory(inventory)

print(result["product_quantities"])
print(result["top_warehouse"])
print(result["stock_everywhere"])
print(result["stock_in_one_warehouse"])
print(result["top_category"])
