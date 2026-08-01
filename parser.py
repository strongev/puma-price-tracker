from bs4 import BeautifulSoup


def parse_products(html: str):
    soup = BeautifulSoup(html, "lxml")

    products = []

    for product in soup.select("div.product-item"):

        name_element = product.select_one("a.product-item__name")

        if not name_element:
            continue

        price_element = product.select_one("[data-price-amount]")

        products.append({
            "name": name_element.get_text(strip=True),
            "price": int(float(price_element["data-price-amount"])) if price_element else 0,
            "url": name_element["href"],
            "sku": product.get("data-product-sku", "")
        })

    return sorted(products, key=lambda x: x["price"])