from django.contrib import admin

from .models import Product, Order, Item


class OrderInline(admin.TabularInline):
    model = Item


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(Product)
