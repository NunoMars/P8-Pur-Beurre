import json
import requests
from django.test import TestCase
from .clear_data import (
    clean_data,
    eliminate_duplicate_products,
)

from .download_products import DataFiles

    
class DownloadProducts(TestCase):
    def test_call_openfoodfacts(self):
        with open("products_data.json") as products_data:
            results_test = json.load(products_data)

        assert DataFiles.all_products == results_test

        with open('products_data_eliminate_duplicated.json') as products_data_eliminated_products:
            results_test = json.load(products_data_eliminated_products)

        assert DataFiles.products_to_inser == results_test