from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

from checkout.models import Order
from plans.models import UserPlan

from .forms import UserProfileForm
from .models import UserProfile


@login_required
def profile(request):
    """Display the user's profile."""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
        else:
            messages.error(request, "Update failed. Please ensure the form is valid.")
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    # ChatGPT Code
    user_plans = UserPlan.objects.filter(user=request.user).select_related("plan")

    template = "profiles/profile.html"
    context = {
        "form": form,
        "orders": orders,
        "user_plans": user_plans,
        "on_profile_page": True,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (
            f"This is a past confirmation for order number {order_number}."
            "A confirmation email was sent on the order date."
        ),
    )

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
    }

    return render(request, template, context)
