from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_shoppingbag, name="view_shoppingbag"),
    path('add/<product_id>/', views.add_to_bag, name='add_to_bag'),
]