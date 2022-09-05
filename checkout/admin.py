from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdmin(admin.ModelAdmin):
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_total', 'order_number',)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLineItem, OrderLineItemAdmin)
