from config import URL
from scraper import get_html
from parser import parse_products
from notifier import send_message


html = get_html(URL)

products = parse_products(html)

message = "Puma Price Tracker\n\n"
message += "Топ-3:\n\n"

for i, product in enumerate(products[:3], start=1):
    message += (
        f"{i}. {product['name']}\n"
        f"💰 {product['price']} грн\n"
        f"{product['url']}\n\n"
    )

print(message)

send_message(message)

for i, product in enumerate(products[:3], start=1):
    print(f"{i}. {product['name']}")
    print(f"   Цена: {product['price']} грн")
    print(f"   SKU: {product['sku']}")
    print(f"   {product['url']}")
    print()