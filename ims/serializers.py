from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'category', 'total_quantity', 'quantity_left', 'quantity_sold', 'price', 'labels', 'uuid', 'created_at']
        extra_kwargs = {
            'quantity_left': {'read_only': True},
            'quantity_sold': {'read_only': True},
            'created_at': {'read_only': True}
        }
    

