from django.urls import path

from .views import (
                        product_create_view,
                        product_detail_view,
                        product_edit_view,
                    )

urlpatterns = [
    path('products/', product_create_view, name="new_product"),
    path('products/<str:uuid>/', product_detail_view, name="product"),
    path('products/<str:uuid>/edit/', product_edit_view, name="edit_product"),
]