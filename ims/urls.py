from django.urls import path

from .views import (
                        product_create_view,
                        product_detail_view,
                    )

urlpatterns = [
    path('new_product/', product_create_view, name="new_product"),
    path('product/<str:uuid>/', product_detail_view, name="product"),
]