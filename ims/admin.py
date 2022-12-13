from django.contrib import admin

from .models import Product, Order, OrderItem


class OrderInline(admin.TabularInline):
    model = OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(Product)
