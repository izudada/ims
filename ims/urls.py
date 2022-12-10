from django.urls import path

from .views import (
                        product_create_view,
                    )

urlpatterns = [
    path('new_product/', product_create_view, name="new_product"),
]