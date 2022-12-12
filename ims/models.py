from django.db import models
from jsonfield import JSONField


class TrackingModel(models.Model):
    """
        Most of the models have have these two fields below as recurrent fields, 
        so to maintain a dry code it is wise to separate them this way.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True
        ordering = ('-created_at',)


class Product(TrackingModel, models.Model):
    name = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=200)
    total_quantity = models.IntegerField(default=0)
    quantity_left = models.IntegerField(default=0)
    quantity_sold = models.IntegerField(default=0)
    price = models.FloatField()
    labels = models.JSONField(null=True)
    uuid = models.UUIDField(null=True)

    def __str__(self):
        return self.name


class Order(TrackingModel, models.Model):
    uuid = models.UUIDField(null=True)
    paid = models.BooleanField(default=False)
    total = models.IntegerField()

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.paid}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.IntegerField()
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
