from django.shortcuts import render
from django.db.models import Min
from .models import Product

# Create your views here.
def all_products(request):
    """ A view to show list of all Products"""
# ChatGPT Update
    products = (
        Product.objects.filter(is_active=True)
        .select_related("category")
        .annotate(from_price=Min("variants__price"))
    )

    context = {
        'products': products
    }
    
    return render(request, 'merchandise/products.html', context)