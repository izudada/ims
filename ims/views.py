from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Product
from .serializers import ProductSerializer
import uuid as my_uuid


class ProductAPIView(ListCreateAPIView):
    """
        This class defines the create and get
        behavior of product api.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        return serializer.save(
            uuid=my_uuid.uuid4(), 
            quantity_left=self.request.data['total_quantity']
        )

    def get_queryset(self):
        return Product.objects.filter(uuid=self.request.data['uuid'])
