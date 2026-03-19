from django.shortcuts import render, redirect
from .models import ShoppingBagItem

# Create your views here.

def view_shoppingbag(request):
    """ A view to show the shopping bag contents """
    bag_items = ShoppingBagItem.objects.filter(user=request.user)
    grand_total = sum(item.product.from_price for item in bag_items)

    context = {
        'bag_items': bag_items,
        'grand_total': grand_total,
    }

    return render(request, 'shoppingbag/shoppingbag.html', context)

def add_to_bag(request, product_id):
    """ A view to allow users to add products to shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if product_id in list(bag.keys()):
        bag[product_id] += quantity
    else:
        bag[product_id] = quantity

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)
