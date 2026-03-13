from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Min
from .models import Product

# Claude AI Code
def all_products(request):
    """A view to show all products, including search and category filtering"""

    products = (
        Product.objects.filter(is_active=True)
        .select_related("category")
        .annotate(from_price=Min("variants__price"))
    )

    query = None
    current_category = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower("name"))
            elif sortkey == 'price':
                sortkey = 'from_price'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    if request.GET:
        if "category" in request.GET:
            current_category = request.GET["category"].strip()

            category_list = [c.strip() for c in current_category.split(",") if c.strip()]
            products = products.filter(category__name__in=category_list)

        if "q" in request.GET:
            query = request.GET["q"].strip()

            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("merchandise:products"))

            queries = (
                Q(title__icontains=query) |
                Q(vendor__icontains=query) |
                Q(tags__icontains=query) |
                Q(category__name__icontains=query)
            )

            products = products.filter(queries).distinct()

    current_sorting = f'{sort}_{direction}'

    context = {
        "products": products,
        "search_term": query,
        "current_category": current_category,
    }

    return render(request, "merchandise/products.html", context)


def product_detail(request, product_id):
    """A view to show individual products"""

    product = get_object_or_404(
        Product.objects.annotate(from_price=Min("variants__price")),
        pk=product_id
    )

    return render(request, "merchandise/product_detail.html", {"product": product})