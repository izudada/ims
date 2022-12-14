from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import (
                        ProductAPIView,
                        ProductDetailAPIView,
                        CartAPI,
                        checkout,
                        order_detail,
                        orders
                    )
from ..models import Product


class TestUrls(SimpleTestCase):

    def test_api_products_resolves(self):
        url = reverse('products')
        self.assertEquals(resolve(url).func.view_class, ProductAPIView)
    
    def test_api_product_resolves(self):
        url = reverse('product', kwargs={'uuid': "330a0d58-04d1-4cf7-8380-ce9e22990445"})
        self.assertEquals(resolve(url).func.view_class, ProductDetailAPIView)

    def test_api_cart_resolves(self):
        url = reverse('cart')
        self.assertEquals(resolve(url).func.view_class, CartAPI)
    
    def test_api_checkout_resolves(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, checkout)

    def test_api_order_detail_resolves(self):
        url = reverse('order', kwargs={'uuid': "fa3a4cc7-dd6e-46e4-9653-c981a9812db5"})
        self.assertEquals(resolve(url).func, order_detail)

    def test_api_orders_resolves(self):
        url = reverse('orders')
        self.assertEquals(resolve(url).func, orders)
