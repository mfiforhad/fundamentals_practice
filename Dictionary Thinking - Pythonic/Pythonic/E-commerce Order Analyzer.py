from collections import Counter

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

def analyze_orders(orders):
    customers = {}
    product_sales = Counter()

    for order in orders:
        customer_name = order["customer"]

        if customer_name not in customers:
            customers[customer_name] = {
                "orders": 0,
                "items_bought": Counter(),
                "total_spent": 0,
            }

        customer = customers[customer_name]
        customer["orders"] += 1

        for product, quantity, price in order["items"]:
            customer["items_bought"][product] += quantity
            customer["total_spent"] += quantity * price

            product_sales[product] += quantity

    return customers, product_sales


customers, product_sales = analyze_orders(orders)


# Customer who spent the most
top_customer = max(
    customers.items(),
    key=lambda item: item[1]["total_spent"],
)

# Product sold the most
top_product = product_sales.most_common(1)[0]

# Products belonging to each customer
products_by_customer = {
    name: set(data["items_bought"]) for name, data in customers.items()
}

rahim_products = products_by_customer["Rahim"]
karim_products = products_by_customer["Karim"]

both = rahim_products & karim_products
only_one = rahim_products ^ karim_products
