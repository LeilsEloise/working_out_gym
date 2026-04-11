from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.
# ChatGPT Code
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    extra = 0
    fields = ('product_variant', 'quantity', 'lineitem_total')
    readonly_fields = ('lineitem_total',)
    autocomplete_fields = ['product_variant']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related(
            'product_variant', 'product_variant__product'
        )

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
# ChatGPT Code
    readonly_fields = (
        'order_number',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_bag', 
        'stripe_pid',
    )

    fields = (
        'order_number',
        'full_name',
        'email',
        'phone_number',
        'country',
        'postcode',
        'town_or_city',
        'street_address1',
        'street_address2',
        'county',
        'date',
        'delivery_cost',
        'order_total',
        'grand_total',
        'original_bag', 
        'stripe_pid',
    )
    
    list_display = ('order_number', 'date', 'full_name', 'order_total', 'delivery_cost', 'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)