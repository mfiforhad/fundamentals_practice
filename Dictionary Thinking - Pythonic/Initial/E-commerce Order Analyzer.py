"""
Build a program that produces:
{
    "Rahim": {
        "orders": 2,
        "items_bought": {"Laptop": 1, "Mouse": 3, "Monitor": 2},
        "total_spent": 1240,
    },
    "Karim": {
        "orders": 1,
        "items_bought": {"Keyboard": 1, "Mouse": 1},
        "total_spent": 70,
    },
}
"""

orders = [
    {
        "order_id": 101,
        "customer": "Rahim",
        "items": [("Laptop", 1, 800), ("Mouse", 2, 20)],
    },
    {
        "order_id": 102,
        "customer": "Karim",
        "items": [("Keyboard", 1, 50), ("Mouse", 1, 20)],
    },
    {
        "order_id": 103,
        "customer": "Rahim",
        "items": [("Monitor", 2, 200), ("Mouse", 1, 20)],
    },
]
customers: dict[str, dict] = {
    item["customer"]: {"orders": 0, "items_bought": {}, "total_spent": 0}
    for item in orders
}

for order in orders:
    # print(order["items"])
    for customer, order_items in customers.items():
        # print(order_items)
        if customer == order["customer"]:
            order_items["orders"] = order_items.get("orders", 0) + 1
            for product, qty, price in order["items"]:
                order_items["items_bought"].setdefault(product, 0)
                for item in order_items["items_bought"].keys():
                    # print(item)
                    if item == product:
                        order_items["items_bought"][item] += qty
                total_price = qty * price
                # print(f"{customer}: {product} = qty {qty} price {price} and after total {total_price}")
                order_items["total_spent"] += total_price

print(customers)

customer_spent_most = max(customers, key=lambda x: customers[x]["total_spent"])

print(customer_spent_most)


product_summary = {}

for order in orders:
    for item in order["items"]:
        product_summary.setdefault(item[0], 0)
        # product_summary[item[0]] = 0
        product_summary[item[0]] += item[1]

print(product_summary)
product_sold_most = max(product_summary, key=lambda x: product_summary[x])
print(product_sold_most)


buy_sumarry = {
    key: {x for x in customers[key]["items_bought"].keys()} for key in customers.keys()
}

both_customer_bought = buy_sumarry["Rahim"] & buy_sumarry["Karim"]

brought_by_one = buy_sumarry["Rahim"] ^ buy_sumarry["Karim"]

print(f"both_customer_bought: {both_customer_bought}")
print(f"brought_by_one: {brought_by_one}")
