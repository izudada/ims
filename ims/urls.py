from django.urls import path

from .views import (
                        product_create_view,
                        product_detail_view,
                        product_edit_view,
                        product_delete_view,
                        ProductListView,
                    )

urlpatterns = [
    path('products/', product_create_view, name="new_product"),
    path('products/all/', ProductListView.as_view(), name="all_product"),
    path('products/<str:uuid>/', product_detail_view, name="product"),
    path('products/<str:uuid>/edit/', product_edit_view, name="edit_product"),
    path('products/<str:uuid>/delete/', product_delete_view, name="delete_product"),

]