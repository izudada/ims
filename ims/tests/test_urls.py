from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import (
                        product_create_view,
                        product_detail_view,
                        product_edit_view,
                        product_delete_view,
                        ProductListView,
                    )
from ..models import Product


class TestUrls(SimpleTestCase):

    def test_api_new_product_resolves(self):
        url = reverse('new_product')
        self.assertEquals(resolve(url).func, product_create_view)

    def test_api_product_detail_view_resolves(self):
        url = reverse('product', kwargs={'uuid':'5db86260-b895-48b2-83b4-cea28f085366'})
        self.assertEquals(resolve(url).func, product_detail_view)

    def test_api_product_edit_view_resolves(self):
        url = reverse('edit_product', kwargs={'uuid':'5db86260-b895-48b2-83b4-cea28f085366'})
        self.assertEquals(resolve(url).func, product_edit_view)

    def test_api_product_delete_view_resolves(self):
        url = reverse('delete_product', kwargs={'uuid':'5db86260-b895-48b2-83b4-cea28f085366'})
        self.assertEquals(resolve(url).func, product_delete_view)

    def test_api_product_list_view_resolves(self):
        url = reverse('all_product')
        self.assertEquals(resolve(url).func.view_class, ProductListView)