import csv
from datetime import date,datetime

def export_expiring_products(json_data, filename, days):
# Вывести товары, срок годности которых истекает в ближайшие `days` дней.
    today = date.today()
    with open(filename, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "category", "expires", "days_left"])
        for product in json_data["products"]:
            expires = datetime.strptime(product["expires"], "%Y-%m-%d").date()
            dayleft = (expires - today).days
            if 0 <= dayleft < days:
                writer.writerow([
                    product["id"],
                    product["name"],
                    product["category"],
                    product["expires"],
                    dayleft
                ])


def export_expired_products(json_data, filename):
# Вывести товары, у которых срок годности уже истёк.
    today = date.today()
    with open(filename, "w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(["id", "name", "category", "expires", "expired_days_ago"])
            for product in json_data["products"]:
                expires = datetime.strptime(product["expires"], "%Y-%m-%d").date()
                expired_days = (today - expires).days
                if 0 < expired_days:
                    writer.writerow([
                        product["id"],
                        product["name"],
                        product["category"],
                        product["expires"],
                        expired_days
                    ])


def export_sales_report(json_data, filename):
# Создать отчёт по продажам: название товара, количество проданных единиц, общая выручка.

    products = {
        product["id"]: product
        for product in json_data["products"]
    }
    sales = json_data["sales"]
    sales_total = {}
    for sale in sales:
        product_id = sale["product_id"]
        quantity = sale["quantity"]      
        if product_id not in sales_total:
            sales_total[product_id] = 0
        sales_total[product_id] += quantity

    with open(filename, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(["product_name", "quantity_sold", "total_revenue"])
        for product_id, total_quantity in sales_total.items():
            product = products[product_id]
            total_revenue = product["price"] * total_quantity
            writer.writerow([
                product["name"],
                total_quantity,
                f"{total_revenue:.2f}"
            ])
    # print(sales_total)
    
# **CSV‑выход:**  
# `product_name, quantity_sold, total_revenue`

def export_category_summary(json_data, filename):
# Сгруппировать товары по категориям: количество товаров и средняя цена.
    categories = {}
    for product in json_data["products"]:
        category = product["category"] 
        if category not in categories:
            categories[category] = { "count": 0, "total_price": 0 } 
        categories[category]["count"] += 1 
        categories[category]["total_price"] += product["price"]
    with open(filename, "w", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)
            writer.writerow(["category", "products_count", "average_price"])
            for category, data in sorted(categories.items()):
                count = data["count"]
                average_price = data["total_price"] / count
                writer.writerow([
                     category,
                     count,
                     f"{average_price:.2f}"
                ])

