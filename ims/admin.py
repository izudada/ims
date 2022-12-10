from django.contrib import admin

from .models import Category, Label, Product


class LabelInline(admin.TabularInline):
    model = Label


class LabelAdmin(admin.ModelAdmin):
    inlines = [LabelInline]


admin.site.register(Product, LabelAdmin)

admin.site.register(Category)
