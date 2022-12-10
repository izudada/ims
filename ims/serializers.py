from rest_framework import serializers

from .models import Label, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'category', 'total_quantity', 'quantity_left', 'price', 'uuid']


class LabelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Label
        fields = ['product', 'color', 'size', 'uuid']