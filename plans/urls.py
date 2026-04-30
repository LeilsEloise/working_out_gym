from django.urls import path

from . import views

app_name = "plans"

urlpatterns = [
    path("", views.plans_list, name="plans"),
    path("buy/<int:plan_id>/", views.buy_plan, name="buy_plan"),
]
