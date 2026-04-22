from django.urls import path
from . import views

app_name = "merchandise"

urlpatterns = [
    path("", views.all_products, name="products"),
    path("<int:product_id>/", views.product_detail, name="product_detail"),
    path("badges/", views.all_badges, name="all_badges"),
    path("badge/<int:badge_id>/", views.badge_detail, name="badge_detail"),
    path("add/", views.add_product, name="add_product"),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]