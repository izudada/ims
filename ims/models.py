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


class Category(TrackingModel, models.Model):
    name = models.CharField(max_length=200)
    uuid = models.UUIDField(null=True)

    def __str__(self):
        return self.name


class Product(TrackingModel, models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, related_name="category", on_delete= models.CASCADE)
    quantity = models.IntegerField()
    price = models.FloatField()
    uuid = models.UUIDField(null=True)

    def __str__(self):
        return self.name


class Label(TrackingModel, models.Model):
    product = models.ForeignKey(Product, related_name="product", on_delete= models.CASCADE)
    color = models.CharField(max_length=200, null=True)
    size = models.CharField(max_length=200, null=True)
    uuid = models.UUIDField(null=True)

    def __str__(self):
        return self.uuid
