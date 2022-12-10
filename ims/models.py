from django.db import models


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
    category = models.CharField(max_length=200, unique=True)
    total_quantity = models.IntegerField(default=0)
    quantity_left = models.IntegerField(default=0)
    quantity_sold = models.IntegerField(default=0)
    price = models.FloatField()
    uuid = models.UUIDField(null=True)

    def __str__(self):
        return self.name


class Label(TrackingModel, models.Model):
    product = models.ForeignKey(Product, related_name="product", on_delete= models.CASCADE, null=True)
    color = models.CharField(max_length=200, null=True)
    size = models.CharField(max_length=200, null=True)
    uuid = models.UUIDField(null=True)

    def __str__(self):
        return str(self.uuid)
