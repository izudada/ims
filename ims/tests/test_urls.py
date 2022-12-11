from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import (
                        ProductAPIView,
                    )
from ..models import Product


class TestUrls(SimpleTestCase):

    def test_api_new_product_resolves(self):
        url = reverse('products')
        self.assertEquals(resolve(url).func.view_class, ProductAPIView)
