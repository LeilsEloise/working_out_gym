from django.shortcuts import render, get_object_or_404
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

def product_detail(request, product_id):
    """ A view to show individual Products"""

    product = get_object_or_404(
        Product.objects.annotate(from_price=Min("variants__price")),
        pk=product_id
    )
    
    return render(request, 'merchandise/product_detail.html', {"product": product})