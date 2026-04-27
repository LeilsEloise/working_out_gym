from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.db.models import Q, Min

from .models import Product, ProductVariant, Category, Badge
from .forms import ProductForm, ProductVariantForm

# ChatGPT Code
def is_superuser(user):
    if not user.is_superuser:
        raise PermissionDenied
    return True

# Claude AI Code
def all_products(request):
    """A view to show all products, including search and category filtering"""

    products = (
        Product.objects.filter(is_active=True)
        .select_related("category")
        .prefetch_related("variants")
        .annotate(min_price=Min("variants__price"))
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
                sort = '-min_price'
            else:
                sort = 'min_price'
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

    paginator = Paginator(products, 100)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "products": page_obj,
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
        Product.objects.prefetch_related("variants").annotate(from_price=Min("variants__price")),
        pk=product_id
    )
    min_price = product.variants.order_by('price').first().price if product.variants.exists() else None

    current_categories = Category.objects.all()
    active_badges = Badge.objects.filter(is_active=True)

    context = {
        "product": product,
        'min_price': min_price,
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

@login_required
@user_passes_test(is_superuser)
# ChatGPT Code
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()

        # ChatGPT Code
        sizes = form.cleaned_data.get('size')

        if product.has_sizes and sizes:
            size_list = [s.strip() for s in sizes.split(',') if s.strip()]

            for size in size_list:
                ProductVariant.objects.create(
                    product=product,
                    price=form.cleaned_data['price'],
                    size=size,
                    variant_title=size,
                )
        else:
            # No sizes → single variant
            ProductVariant.objects.create(
                product=product,
                price=form.cleaned_data['price'],
                size=None,
                variant_title="Default",
            )

            messages.success(request, 'Successfully added product!')
            return redirect('merchandise:product_detail', product_id=product.id)
    else:
        form = ProductForm()

    return render(request, 'merchandise/add_product.html', {'form': form})

@login_required
@user_passes_test(is_superuser)
# Code Institute Code
def edit_product(request, product_id):
    """ Edit a product in the Merchandise app """
    product = get_object_or_404(Product, pk=product_id)
    # ChatGPT Code
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            product = form.save()

            for variant in product.variants.all():
                variant.price = form.cleaned_data['price']
                variant.save()

            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('merchandise:product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        variant = product.variants.first()
        initial_data = {}

        if variant:
            initial_data['price'] = variant.price

        form = ProductForm(instance=product, initial=initial_data)
        messages.info(request, f'You are editing {product.title}')

    template = 'merchandise/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

@login_required
@user_passes_test(is_superuser)
# ChatGPT Code
def delete_product(request, product_id):
    """Delete a product from the Merchandise app"""

    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully!')
        return redirect(reverse('merchandise:products'))

    messages.error(request, 'Invalid request')
    return redirect(reverse('merchandise:product_detail', args=[product.id]))