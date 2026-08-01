# services.py
from config import URL
from scraper import get_html
from parser import parse_products
from storage import load_history, save_history

def check_prices_and_get_message():
    html = get_html(URL)
    products = parse_products(html)
    old_products = load_history()

    message = "Puma Price Tracker\n\n"
    message += "Топ-3:\n\n"

    for i, product in enumerate(products[:3], start=1):
        message += (
            f"{i}. {product['name']}\n"
            f"💰 {product['price']} грн\n"
            f"{product['url']}\n\n"
        )

    if not old_products:
        save_history(products)
    
    return message