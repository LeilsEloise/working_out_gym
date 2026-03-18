from django.shortcuts import render
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