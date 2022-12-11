from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'category', 'total_quantity', 'quantity_left', 'price', 'labels', 'uuid']
