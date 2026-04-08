from decimal import Decimal
from django.conf import settings
from merchandise.models import ProductVariant


def bag_contents(request):
    bag_items = []
    total = Decimal('0.00')
    product_count = 0
    bag = request.session.get('bag', {})

    for variant_id, quantity in bag.items():
        variant = ProductVariant.objects.filter(pk=variant_id).first()

        if not variant:
            continue  # skip broken/old session items

        subtotal = quantity * variant.price
        total += subtotal
        product_count += quantity

        bag_items.append({
            'variant_id': variant_id,
            'quantity': quantity,
            'product': variant.product,
            'variant': variant,
            'price': variant.price,
            'subtotal': quantity * variant.price,
        })

    # Delivery calculations
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')

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