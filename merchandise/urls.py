from django.urls import path
from . import views

app_name = "merchandise"

urlpatterns = [
    path("", views.all_products, name="products"),
]