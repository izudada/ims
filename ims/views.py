from rest_framework.exceptions import APIException
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework import status
import uuid as my_uuid
from .models import Product, Order, Item
from .serializers import ProductSerializer, OrderSerializer, OrderItemSerializer


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
            quantity_left=serializer.validated_data.get("total_quantity"), # set qty_left as total qty
            price=int(serializer.validated_data.get("price") * 100), #   kobo quivalence
            uuid=my_uuid.uuid4()
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
        #   get product to make calculations on quantites before updating
        product = Product.objects.get(uuid=self.kwargs['uuid'])

        #   check if serilizer is valid
        # if serializer.validated_data.get("total_quantity") 
        if serializer.is_valid():
            quantity_left = serializer.validated_data.get("total_quantity") - product.quantity_sold
            return serializer.save(quantity_left=quantity_left)
        else:
            return Response({'error': serializer.error}, status=status.HTTP_406_NOT_ACCEPTABLE)


class CartAPI(GenericAPIView):
    """
        Cart API for creating, retrieving, editing and removing cart and item
    """

    def get(self, request, *args, **kwargs):
        if 'cart' in self.request.session:
            result = self.request.session.get('cart')
            return Response(result, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No existing cart'}, status=status.HTTP_404_NOT_FOUND)

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
        
    def delete(self, request, *args, **kwargs):
        del self.request.session['cart']
        return Response({'message': 'cart deleted successfully'},  status=status.HTTP_200_OK)


@api_view(['POST',])
def  checkout(request):
    """
        This class defines the create
        behavior of checkout api.
    """
    #   Check if cart exist before checking put
    if 'cart' in request.session:
        cart = request.session.get('cart')
        total = [value['sub_total'] for key, value in cart.items() ]

        #   Create order
        order = Order(
            uuid=my_uuid.uuid4(),
            paid=True,
            total=sum(total)
        )
        order.save()

        #   Create order Items
        for prod, value in cart.items():
            product = Product.objects.get(uuid=prod)
            item = Item(
                order=order,
                product=product,
                sub_total=value['sub_total'],
                quantity=value['quantity']
            )
            item.save()

        del request.session['cart']
        return Response({'order': order.uuid},  status=status.HTTP_201_CREATED)

    else:
        return Response({"error": "No cart exists for checkout"},  status=status.HTTP_404_NOT_FOUND)

@api_view(['GET',])
def order_detail(request, uuid):
    """
        Endpoint to get the detail of an order
    """
    data = {}
    try:
        order = Order.objects.get(uuid=uuid)
    except Order.DoesNotExist:
        return Response({'error: order not found'}, status=status.HTTP_404_NOT_FOUND)
    
    order_serializer = OrderSerializer(order)
    data['order'] = order_serializer.data
    items = order.get_items()
    data['items'] = []
    for item in items:
        item_serializer = OrderItemSerializer(item)
        data['items'].append(item_serializer.data)
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET',])
def orders(request):
    """
        Endpoint to get all orders
    """
    try:
        orders = Order.objects.filter().all()
    except Order.DoesNotExist:
        return Response({'error: no order record exists yet'}, status=status.HTTP_404_NOT_FOUND)
    
    orders_serializer = OrderSerializer(orders, many=True)
    return Response(orders_serializer.data, status=status.HTTP_200_OK)