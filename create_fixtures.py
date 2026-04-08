import csv
import json

from django.utils.text import slugify

existing_category_slugs = set()

def unique_slug(name, existing_slugs):
    base = slugify(name) or "category"
    slug = base
    i = 1

    while slug in existing_slugs:
        i += 1
        slug = f"{base}-{i}"

    existing_slugs.add(slug)
    return slug

INPUT_CSV = "merchandise/data/gymshark_products.csv"

categories = {}
products = {}
variants = []

category_map = {}
product_map = {}

existing_category_slugs = set()

category_id = 1
product_id = 1
variant_id = 1

with open(INPUT_CSV, newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)

for row in reader:
    # --- CATEGORY ---
    category_name = (row.get("product_type") or "Uncategorized").strip()

    if category_name not in category_map:
        category_map[category_name] = category_id

        slug = unique_slug(category_name, existing_category_slugs)

        categories[category_id] = {
            "model": "merchandise.category",
            "pk": category_id,
            "fields": {
                "name": category_name,
                "slug": slug,
            },
        }

        category_id += 1

    cat_id = category_map[category_name]

    # --- PRODUCT ---
    product_key = (row.get("handle") or row.get("title") or "").strip().lower()

        if product_key not in product_map:
            product_map[product_key] = product_id

            variant_title = row.get("variant_title", "")
            category_name = (row.get("product_type") or "").lower()

            clothing_keywords = ["shirt", "top", "tank", "hoodie", "jacket", "shorts", "leggings", "joggers"]
            size_keywords = ["xs", "s", "m", "l", "xl", "xxl"]

            variant_title_clean = variant_title.lower()

            is_clothing = any(word in category_name for word in clothing_keywords)
            has_size_word = any(size in variant_title_clean for size in size_keywords)

            has_sizes = is_clothing and has_size_word

            products[product_id] = {
                "model": "merchandise.product",
                "pk": product_id,
                "fields": {
                    "title": row["title"],
                    "handle": row["handle"],
                    "slug": row["handle"],
                    "category": cat_id,
                    "vendor": row.get("vendor", ""),
                    "tags": row.get("tags", ""),
                    "image_src": row.get("image_src", ""),
                    "has_sizes": has_sizes,
                    "is_active": True,
                }
            }

            product_id += 1

        prod_id = product_map[product_key]

        # --- VARIANT ---
        variant = {
            "model": "merchandise.productvariant",
            "pk": variant_id,
            "fields": {
                "product": prod_id,
                "variant_title": row.get("variant_title", ""),
                "sku": row.get("sku") or None,
                "price": float(row.get("price") or 0),
                "inventory_quantity": int(row.get("inventory_quantity") or 0),
                "image_src": row.get("image_src", ""),
                "is_active": True,
            }
        }

        variants.append(variant)
        variant_id += 1

# --- SAVE FILES ---
with open("categories.json", "w", encoding="utf-8") as f:
    json.dump(list(categories.values()), f, indent=2)

with open("products.json", "w", encoding="utf-8") as f:
    json.dump(list(products.values()), f, indent=2)

with open("variants.json", "w", encoding="utf-8") as f:
    json.dump(variants, f, indent=2)

print("✅ Fixtures generated successfully!")
