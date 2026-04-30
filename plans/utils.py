from .models import UserPlan


def can_purchase_plan(user, plan):
    if plan.plan_type == "fitness":
        return not UserPlan.objects.filter(
            user=user, plan__plan_type="fitness"
        ).exists()

    if plan.plan_type == "nutrition":
        return not UserPlan.objects.filter(
            user=user, plan__plan_type="nutrition"
        ).exists()

    return False
