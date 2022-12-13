from django.urls import path
from .views import (
                        ProductAPIView,
                        ProductDetailAPIView,
                        CartAPI,
                        checkout,
                    )

urlpatterns = [
    path("products/cart/checkout/", checkout, name="checkout"),
    path("products/cart/", CartAPI.as_view(), name="cart"),
    path("products/", ProductAPIView.as_view(), name="products"),
    path("products/<str:uuid>/", ProductDetailAPIView.as_view(), name="product"),
]