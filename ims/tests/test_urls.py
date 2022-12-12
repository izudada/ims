from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import (
                        ProductAPIView,
                        ProductDetailAPIView
                    )
from ..models import Product


class TestUrls(SimpleTestCase):

    def test_api_products_resolves(self):
        url = reverse('products')
        self.assertEquals(resolve(url).func.view_class, ProductAPIView)
    
    def test_api_product_resolves(self):
        url = reverse('product', kwargs={'uuid': "330a0d58-04d1-4cf7-8380-ce9e22990445"})
        self.assertEquals(resolve(url).func.view_class, ProductDetailAPIView)
