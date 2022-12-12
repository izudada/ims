from django.urls import path
from .views import (
                        ProductAPIView,
                        ProductDetailAPIView,
                        CartAPI,
                    )

urlpatterns = [
    path("products/cart/", CartAPI.as_view(), name="cart"),
    path("products/", ProductAPIView.as_view(), name="products"),
    path("products/<str:uuid>/", ProductDetailAPIView.as_view(), name="product"),
]