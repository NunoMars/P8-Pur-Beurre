from django.apps import apps
from django.test import TestCase
from products.apps import ProductsConfig


class ProductsConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(ProductsConfig.name, 'products')
        self.assertEqual(apps.get_app_config('products').name, 'products')