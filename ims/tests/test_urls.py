from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import (
                        product_create_view,
                        product_detail_view
                    )


class TestUrls(SimpleTestCase):

    def test_api_new_product_is_resolved(self):
        url = reverse('new_product')
        self.assertEquals(resolve(url).func, product_create_view)

    def test_api_product_detail_view_is_resolved(self):
        url = reverse('product', kwargs={'uuid':'5db86260-b895-48b2-83b4-cea28f085366'})
        self.assertEquals(resolve(url).func, product_detail_view)