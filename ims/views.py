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
                - product_uuid = uuid for product
                - data = data to be retuned
                - product_serializer = serializer for product data
                - label_uuid = uuid for labels
                - label_serializer = serializer for label data
                - product = instance of product 
    """
    # product uuid object
    product_uuid = my_uuid.uuid4()

    data = {}

    product_serializer = ProductSerializer(data=request.data['product'])

    #   Check if product serializer is valid
    if product_serializer.is_valid():

        #   save or create product
        product_serializer.save(
            uuid=product_uuid, quantity_left=request.data['product']['total_quantity']
        )
        data['product'] = product_serializer.data

        #   if label exist validate using label serializer
        if "label" in request.data:
            # label uuid object
            label_uuid = my_uuid.uuid4()
            label_serializer = LabelSerializer(data=request.data['label'])

            try:
                if label_serializer.is_valid():
                    #   save or create serializer
                    try:
                        product = Product.objects.get(name=request.data['product']['name'])
                    except Exception as e:
                        print(e)
                        return Response({"error": e})

                    label_serializer.save(product=product, uuid=label_uuid)
                    data['label'] = label_serializer.data
            except Exception as e:
                print(e)
                return Response(label_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(data=data, status=status.HTTP_201_CREATED)

@api_view(['GET',])
def product_detail_view(request, uuid):
    """
        Endpoint to get the detail of a product

        variables:
            - data = result to be returned on 201
            - product = instance of product
            - labels = labels related to product
    """
    data = {}
    try:
        product = Product.objects.get(uuid=uuid)
        data['product'] = ProductSerializer(product).data
        
        try:
            labels = Label.objects.filter(product=product).all()
            print(labels)
            data['label'] = LabelSerializer(labels, many=True).data
        except Exception as e:
            print(e)

        return Response(data, status=status.HTTP_200_OK)
    except Product.DoesNotExist:
        return Response(data={"error": "product does not exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT',])
def product_edit_view(request, uuid):
    data = {}
    try:
        #   Check if product exists
        product = Product.objects.get(uuid=uuid)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    product_serializer = ProductSerializer(product, data=request.data['product'])

    if product_serializer.is_valid():            

        #   Block runs if label exists in the payload
        if "label" in request.data:
            #   Loop each label to serialize
            for num in range(0, len(request.data['label'])):
                #   Check if label exists
                try:
                    label = Label.objects.get(uuid=request.data['label'][num]['uuid'])
                except Product.DoesNotExist:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                
                label_serializer = LabelSerializer(label, data=request.data['label'][num])
                try:
                    if label_serializer.is_valid():  
                        #   Save Each label serializer
                        label_serializer.save()
                        data['label'] = label_serializer.data

                except Exception as e:
                    print(e)
                    return Response(label_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        #   Save product serializer
        product_serializer.save()
        data['product'] = product_serializer.data

        return Response(data, status=status.HTTP_200_OK)

    return Response(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def product_delete_view(request, uuid):
    """
        Api view that deletes a product

        variables:
            - product = Product instance
            - action = holds th e delete action/method
            - data = return message
    """
    try:
        #   Check if product exists
        product = Product.objects.get(uuid=uuid)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    action = product.delete()
    data = {}

    #   Check if action was sucessful or not
    if action:
        data["success"] = "delete successful"
    else:
        data["failure"] = "delete failed"
    return Response(data=data)


class ProductListView(ListAPIView):
    """
        Api view that returns a paginated list of all products
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'category', 'price', 'uuid')
