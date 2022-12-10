from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Label, Product
from .serializers import LabelSerializer, ProductSerializer
import uuid as my_uuid


@api_view(['POST',])
def product_create_view(request):
    """
        An endpoint to create a product item

        variables:
    """
    # product uuid object
    product_uuid = my_uuid.uuid4()

    data = {}

    product_serializer = ProductSerializer(data=request.data['product'])

    #   Check if product serializer is valid
    if product_serializer.is_valid():
        #   if label exist validate using label serializer
        if request.data['label']:
            # label uuid object
            label_uuid = my_uuid.uuid4()
            label_serializer = LabelSerializer(data=request.data['label'])

            try:
                if label_serializer.is_valid():

                    #   save or create product
                    product_serializer.save(uuid=product_uuid)
                    data['product'] = product_serializer.data

                    #   save or create serializer
                    try:
                        product = Product.objects.get(name=request.data['product']['name'])
                        print(product.name)
                    except Exception as e:
                        print(e)
                        return Response({"error": e})

                    label_serializer.save(product=product, uuid=label_uuid)
                    data['label'] = label_serializer.data
            except Exception as e:
                print(e)
                return Response(label_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data=data, status=status.HTTP_201_CREATED)

