from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .models import Plan, UserPlan
from .utils import can_purchase_plan


# ChatGPT Code
def plans_list(request):
    plans = Plan.objects.all()

    fitness_plans = plans.filter(plan_type="fitness")
    nutrition_plans = plans.filter(plan_type="nutrition")

    has_fitness_plan = False
    has_nutrition_plan = False

    if request.user.is_authenticated:
        user_plans = UserPlan.objects.filter(user=request.user)

        has_fitness_plan = user_plans.filter(plan__plan_type="fitness").exists()
        has_nutrition_plan = user_plans.filter(plan__plan_type="nutrition").exists()

    return render(
        request,
        "plans/plans.html",
        {
            "fitness_plans": fitness_plans,
            "nutrition_plans": nutrition_plans,
            "has_fitness_plan": has_fitness_plan,
            "has_nutrition_plan": has_nutrition_plan,
        },
    )


# ChatGPT Code
def buy_plan(request, plan_id):
    plan = get_object_or_404(Plan, id=plan_id)

    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to purchase a plan.")
        return redirect("account_login")

    if not can_purchase_plan(request.user, plan):
        messages.error(request, "You already own this type of plan.")
        return redirect("plans")

    # store plan in session
    request.session["plan_purchase_id"] = plan.id

    request.session["bag"] = {}

    return redirect("checkout")
