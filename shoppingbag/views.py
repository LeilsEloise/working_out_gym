# ChatGPT Code

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from merchandise.models import Product, ProductVariant
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
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', '/')
    variant_id = request.POST.get('variant_id')

    variant = get_object_or_404(ProductVariant, pk=variant_id)

    bag = request.session.get('bag', {})

    variant_id = str(variant_id)

    if variant_id in bag:
        bag[variant_id] += quantity
        messages.success(
            request,
            f'Updated {variant.product.title} ({variant.variant_title}) quantity to {bag[variant_id]}'
        )
    else:
        bag[variant_id] = quantity
        messages.success(
            request,
            f'Added {variant.product.title} ({variant.variant_title}) to your bag'
        )

    request.session['bag'] = bag
    return redirect(redirect_url)

# ChatGPT Code
def adjust_bag(request, product_id):
    quantity = int(request.POST.get('quantity'))
    variant_id = request.POST.get('variant_id')

    bag = request.session.get('bag', {})
    variant_id = str(variant_id)

    variant = get_object_or_404(ProductVariant, pk=variant_id)

    if quantity > 0:
        bag[variant_id] = quantity
        messages.success(
            request,
            f'Updated {variant.product.title} ({variant.variant_title}) quantity to {quantity}'
        )
    else:
        bag.pop(variant_id)
        messages.success(
            request,
            f'Removed {variant.product.title} ({variant.variant_title}) from your bag'
        )

    request.session['bag'] = bag
    return redirect(reverse('shoppingbag:view_bag'))

# ChatGPT Code
def remove_from_bag(request, product_id):
    try:
        variant_id = request.POST.get('variant_id')
        variant_id = str(variant_id)

        bag = request.session.get('bag', {})

        variant = get_object_or_404(ProductVariant, pk=variant_id)

        bag.pop(variant_id)

        messages.success(
            request,
            f'Removed {variant.product.title} ({variant.variant_title}) from your bag'
        )

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)