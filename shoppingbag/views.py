# ChatGPT Code

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from merchandise.models import Product

# ChatGPT Code
def view_bag(request):
    bag = request.session.get('bag', {})
    bag_items = []
    total = 0

    for product_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=product_id)
        variant = product.variants.first()

        if not variant:
            continue

        subtotal = quantity * variant.price
        total += subtotal

        bag_items.append({
            'product': product,
            'quantity': quantity,
            'price': variant.price,
            'subtotal': subtotal,
        })

    delivery = 3 if total > 0 else 0
    grand_total = total + delivery

    context = {
        'bag_items': bag_items,
        'total': total,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return render(request, 'shoppingbag/shoppingbag.html', context)

def add_to_bag(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    bag = request.session.get('bag', {})

    if product_id in bag:
        bag[product_id] += quantity
        messages.success(request, f'Updated {product.title} quantity')
    else:
        bag[product_id] = quantity
        messages.success(request, f'Added {product.title} to your bag')

    request.session['bag'] = bag

    return redirect(redirect_url)


def adjust_bag(request, product_id):
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[product_id] = quantity
    else:
        bag.pop(product_id)

    request.session['bag'] = bag
    return redirect(reverse('view_shoppingbag'))


def remove_from_bag(request, product_id):
    bag = request.session.get('bag', {})

    bag.pop(product_id, None)

    request.session['bag'] = bag
    return redirect(reverse('view_shoppingbag'))