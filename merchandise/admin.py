from django.contrib import admin

from .models import Category, Product, ProductVariant


# Register your models here.
# Code Institute Boutique Ado code
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)


# ChatGPT Code
class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 0
    fields = ("variant_title", "sku", "price", "inventory_quantity", "is_active")
    readonly_fields = ()
    show_change_link = True


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "handle", "category", "vendor", "is_active")
    list_filter = ("is_active", "category", "vendor")
    search_fields = ("title", "handle", "vendor", "tags")
    ordering = ("title",)
    inlines = [ProductVariantInline]


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "variant_title",
        "sku",
        "price",
        "inventory_quantity",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = ["product__name", "sku"]
    ordering = ("product__title", "variant_title")
