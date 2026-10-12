import json
import store_utils as su

def load_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
  

if __name__ == "__main__":

    products_data = load_json(r"Task 2\products.json")
    sales_data = load_json(r"Task 2\sales.json")
    days = int(input("Введите дни до истечения срока годности: "))
    # result = su.export_expiring_products(products_data, "expiring_products.csv", 10)
    su.export_expiring_products(products_data, "expiring_products.csv", days)
    su.export_expired_products(products_data,"expired_products.csv")
    su.export_category_summary(products_data,"category_summary.csv")

    sales_report_data = {
        "products": products_data["products"],
        "sales": sales_data["sales"]
    }
    su.export_sales_report(sales_report_data,"sales_report.csv")
    # print(sales_report_data)