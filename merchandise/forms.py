from django import forms
from .models import Product, ProductVariant

# ChatGPT Code
class ProductForm(forms.ModelForm):
    price = forms.DecimalField(
        label='Price',
        max_digits=10,
        decimal_places=2,
        required=False 
    )
    size = forms.CharField(
    required=False,
    help_text="Enter sizes separated by commas (e.g. S,M,L,XL)"
    )

    class Meta:
        model = Product
        fields = [
            'title',
            'category',
            'vendor',
            'has_sizes',
            'tags',
            'image',
            'image_src',
            'is_active',
        ]

# ChatGPT Code
class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = ['price']