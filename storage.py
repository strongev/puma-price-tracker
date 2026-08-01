import json
import os

FILE_NAME = "history.json"


def load_history():
    if not os.path.exists(FILE_NAME):
        return {}

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)


def save_history(products):
    data = {}

    for product in products:
        data[product["sku"]] = {
            "name": product["name"],
            "price": product["price"],
            "url": product["url"],
        }

    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)