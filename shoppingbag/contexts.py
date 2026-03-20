from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from merchandise.models import Product

# ChatGPT Code
def bag_contents(request):
    bag_items = []
    total = Decimal('0.00')
    product_count = 0
    bag = request.session.get('bag', {})

    for product_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=product_id)

        if isinstance(item_data, int):
            # Non-sized product
            quantity = item_data
            price = product.variants.first().price if product.variants.exists() else Decimal('0.00')
            subtotal = quantity * price
            total += subtotal
            product_count += quantity

            bag_items.append({
                'product_id': product_id,
                'quantity': quantity,
                'product': product,
                'price': price,
                'subtotal': subtotal,
            })

        else:
            # Product with sizes
            for size, quantity in item_data['items_by_size'].items():
                price = product.variants.first().price if product.variants.exists() else Decimal('0.00')
                subtotal = quantity * price
                total += subtotal
                product_count += quantity
                bag_items.append({
                    'product_id': product_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                    'price': price,
                    'subtotal': subtotal,
                })

    # Delivery calculations
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = total + delivery

    return {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }