from django.urls import path
from .views import (
                        ProductAPIView,
                        ProductDetailAPIView,
                        CartAPI,
                        checkout,
                        order_detail
                    )

urlpatterns = [
    path("cart/checkout/", checkout, name="checkout"),
    path("cart/", CartAPI.as_view(), name="cart"),
    path("products/", ProductAPIView.as_view(), name="products"),
    path("products/<str:uuid>/", ProductDetailAPIView.as_view(), name="product"),
    path("order/<str:uuid>/", order_detail, name="order"),
]