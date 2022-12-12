from rest_framework.exceptions import APIException
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer
import uuid as my_uuid
from rest_framework.decorators import api_view


class ProductAPIView(ListCreateAPIView):
    """
        This class defines the create and list
        behavior of product api.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'category', 'labels')

    def perform_create(self, serializer):
        return serializer.save(
            uuid=my_uuid.uuid4(), 
            quantity_left=serializer.validated_data['total_quantity']
        )


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
        This class defines the update, delete and detail
        behavior of product api.
    """
    serializer_class = ProductSerializer
    lookup_field = "uuid"

    def get_queryset(self):
        return Product.objects.filter(uuid=self.kwargs['uuid'])

    def perform_update(self, serializer):
        # #   get product to make calculations on quantites before updating
        product = Product.objects.get(uuid=self.kwargs['uuid'])
        total_qty = self.request.data['total_quantity']
        qty_left= total_qty - product.quantity_sold


        #   check if new total quantity is less than quantity sold
        if total_qty > product.quantity_sold:
            return serializer.save(
                total_quantity=total_qty,
                quantity_left=qty_left
            )
        else:
            raise APIException("Total quantity must be greater than quantity sold")


class CartAPI(GenericAPIView):
    """
        Cart API for creating, retrieving, editing and removing cart and item
    """

    def get(self, request, *args, **kwargs):
        result = self.request.session.get('cart')
        return Response(result, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        #   Empty cart 
        cart = {}

        #   Loop request data to create cart items
        for item in self.request.data:
            product = Product.objects.get(uuid=item['product'])
            cart[str(product.uuid)] = {
                "quantity": item['quantity'],
                "sub_total": item['quantity'] * product.price
            }
        
        #   save cart items to session
        self.request.session['cart'] = cart
        result = self.request.session.get('cart')

        return Response(result, status=status.HTTP_201_CREATED)
    
    def put(self, request, *args, **kwargs):
        cart = self.request.session['cart']

        #   Update cart if it exists
        if 'cart' in  self.request.session:
            for item in self.request.data:
                product = Product.objects.get(uuid=item['product'])

                #   check if cart item is in cart
                if item['product'] in cart:
                    cart[item['product']]['quantity'] = item['quantity']
                    cart[item['product']]['sub_total'] =  item['quantity'] * product.price

                #   Add item to cart if it doesn't exist
                else:
                    cart[item['product']] = {
                        "quantity": item['quantity'],
                        "sub_total": item['quantity'] * product.price                    
                    }
            
            #   update cart items to session
            result = self.request.session.get('cart')
            return Response(result, status=status.HTTP_200_OK)

        #   Update can't happen if no cart exists
        else:
            return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)
