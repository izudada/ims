from rest_framework import serializers
from .models import Product, Order, Item


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'category', 'total_quantity', 'quantity_left', 'quantity_sold', 'price', 'labels', 'uuid', 'created_at']
        extra_kwargs = {
            'quantity_sold': {'read_only': True},
            'created_at': {'read_only': True}
        }

        def save(self, quantity_left, price, uuid):
            """
                A method overiding DRF serializer's save method
            """
            new_product = Product(
                name = self.validated_data.get("name"),
                category = self.validated_data.get("category"),
                total_quantity = self.validated_data.get("total_quantity"),
                quantity_left = quantity_left, 
                price = price, 
                labels = self.validated_data.get("labels"),
                uuid = uuid
            )
            new_product.save()
            return new_product
    

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['uuid', 'paid', 'total', 'created_at']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['order', 'product', 'sub_total', 'quantity']
