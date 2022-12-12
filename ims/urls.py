from django.urls import path
from .views import (
                        ProductAPIView,
                        ProductDetailAPIView,
                    )

urlpatterns = [
    path("products/", ProductAPIView.as_view(), name="products"),
    path("products/<str:uuid>/", ProductDetailAPIView.as_view(), name="product"),
]