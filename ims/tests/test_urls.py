from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import (
                        product_create_view,
                    )


class TestUrls(SimpleTestCase):

    def test_api_new_product_is_resolved(self):
        url = reverse('new_product')
        self.assertEquals(resolve(url).func, product_create_view)