# ChatGPT Code

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from merchandise.models import Product
from .contexts import bag_contents

# ChatGPT Code
def view_bag(request):
    """
    A view that renders the shopping bag page
    """
    context = bag_contents(request)  # get all totals, items, etc.
    return render(request, 'shoppingbag/shoppingbag.html', context)

# ChatGPT Code
def add_to_bag(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', '/')
    size = request.POST.get('product_size')

    # session keys must be string
    product_id = str(product_id)

    bag = request.session.get('bag', {})

    if size:
        # Ensure the product exists as a dict for sizes
        if product_id in bag:
            if isinstance(bag[product_id], dict):
                # Already has sizes
                bag[product_id]['items_by_size'][size] = bag[product_id]['items_by_size'].get(size, 0) + quantity
            else:
                # Previously added without size → convert it
                bag[product_id] = {'items_by_size': {size: quantity}}
        else:
            # First time adding this product
            bag[product_id] = {'items_by_size': {size: quantity}}

        messages.success(request, f'Added {product.title} (size {size.upper()}) to your bag')

    else:
        # Non-sized products
        if product_id in bag and isinstance(bag[product_id], int):
            bag[product_id] += quantity
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

# ChatGPT Code
def update_bag(request, item_id):
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('product_size')
    bag = request.session.get('bag', {})

    if size:
        if item_id in bag and 'items_by_size' in bag[item_id]:
            if quantity > 0:
                bag[item_id]['items_by_size'][size] = quantity
            else:
                del bag[item_id]['items_by_size'][size]

                if not bag[item_id]['items_by_size']:
                    del bag[item_id]
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            del bag[item_id]

    request.session['bag'] = bag
    messages.success(request, "Bag updated")

    return redirect('shoppingbag:view_bag')