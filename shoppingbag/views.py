# ChatGPT Code

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from merchandise.models import Product
from .contexts import bag_contents
from django.http import HttpResponse

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

    product_id = str(product_id)
    bag = request.session.get('bag', {})

    # ✅ PRODUCTS WITH SIZE
    if size:
        if product_id in bag:
            if isinstance(bag[product_id], dict):
                bag[product_id]['items_by_size'][size] = (
                    bag[product_id]['items_by_size'].get(size, 0) + quantity
                )
                messages.success(
                    request,
                    f'Updated {product.title} (size {size.upper()}) quantity to {bag[product_id]["items_by_size"][size]}'
                )
            else:
                bag[product_id] = {'items_by_size': {size: quantity}}
                messages.success(
                    request,
                    f'Added {product.title} (size {size.upper()}) to your bag'
                )
        else:
            bag[product_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request,
                f'Added {product.title} (size {size.upper()}) to your bag'
            )

    # ✅ PRODUCTS WITHOUT SIZE
    else:
        if product_id in bag and isinstance(bag[product_id], int):
            bag[product_id] += quantity
            messages.success(
                request,
                f'Updated {product.title} quantity to {bag[product_id]}'
            )
        else:
            bag[product_id] = quantity
            messages.success(
                request,
                f'Added {product.title} to your bag'
            )

    request.session['bag'] = bag
    return redirect(redirect_url)

# ChatGPT Code
def adjust_bag(request, product_id):
    """Adjust the quantity of the specified product"""

    product = get_object_or_404(Product, pk=product_id)
    product_id = str(product_id)

    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('product_size')

    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            bag[product_id]['items_by_size'][size] = quantity
            messages.success(
                request,
                f'Updated size {size.upper()} {product.title} quantity to {quantity}'
            )
        else:
            del bag[product_id]['items_by_size'][size]

            if not bag[product_id]['items_by_size']:
                bag.pop(product_id)

            messages.success(
                request,
                f'Removed size {size.upper()} {product.title} from your bag'
            )
    else:
        if quantity > 0:
            bag[product_id] = quantity
            messages.success(
                request,
                f'Updated {product.title} quantity to {quantity}'
            )
        else:
            bag.pop(product_id)
            messages.success(
                request,
                f'Removed {product.title} from your bag'
            )

    request.session['bag'] = bag
    return redirect(reverse('shoppingbag:view_bag'))

# ChatGPT Code
def remove_from_bag(request, product_id):
    """Remove item from shopping bag"""

    try:
        product = get_object_or_404(Product, pk=product_id)
        product_id = str(product_id)

        bag = request.session.get('bag', {})
        size = request.POST.get('product_size')

        if size:
            del bag[product_id]['items_by_size'][size]

            if not bag[product_id]['items_by_size']:
                bag.pop(product_id)

            messages.success(
                request,
                f'Removed size {size.upper()} {product.title} from your bag'
            )
        else:
            bag.pop(product_id)
            messages.success(
                request,
                f'Removed {product.title} from your bag'
            )

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)