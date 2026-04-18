from django import forms
from .models import Product, ProductVariant, Category

# ChatGPT Code
class ProductForm(forms.ModelForm):
    price = forms.DecimalField(label='Price', max_digits=6, decimal_places=2)
    size = forms.CharField(required=False)

    class Meta:
        model = Product
        fields = '__all__'

# ChatGPT Code
class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = ['price']