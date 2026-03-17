from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Min
from .models import Product, Category, Badge

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
    current_categories = Category.objects.all()
    sort = None
    direction = None

    print("Current categories:")
    for category in current_categories:
        print(f"- {category.name}")

    if 'sort' in request.GET:
        sort = request.GET['sort']
        direction = request.GET['direction']
        if sort == 'price':
            if direction == 'desc':
                sort = '-from_price'
            else:
                sort = 'from_price'
        elif sort == 'name':
            if direction == 'desc':
                sort = '-title'
            else:
                sort = 'title'
        elif direction == 'desc':
            sort = f'-{sort}'
        products = products.order_by(sort)

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
        "current_categories": current_categories,
        "product_count": products.count(),
        "badges": Badge.objects.filter(is_active=True),
        "current_sorting": current_sorting,
    }

    return render(request, "merchandise/products.html", context)


def product_detail(request, product_id):
    """A view to show individual products"""

    product = get_object_or_404(
        Product.objects.annotate(from_price=Min("variants__price")),
        pk=product_id
    )

    current_categories = Category.objects.all()
    active_badges = Badge.objects.filter(is_active=True)

    context = {
        "product": product,
        "current_categories": current_categories,
        "active_badges": active_badges,
    }

    return render(request, "merchandise/product_detail.html", context)

# Claude AI Code
def all_badges(request):
    badges = Badge.objects.filter(is_active=True)
    context = {
        "badges": badges,
    }
    return render(request, "merchandise/all_badges.html", context)

# Claude AI Code
def badge_detail(request, badge_id):
    badge = get_object_or_404(Badge, pk=badge_id)
    context = {
        "badge": badge,
    }
    return render(request, "merchandise/badge_detail.html", context)