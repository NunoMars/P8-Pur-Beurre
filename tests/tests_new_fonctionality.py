import json
from django.test import TestCase

from products.new_functionality import insert_products_if_not_in_found_in_data_base

    
class NewFonctionality(TestCase):
    def insert_products_if_not_in_found_in_data_base(self):
        product_tests = 'lactel'


        with open('fixtures/data_new_fonctionality_cleaned_data.json') as products_data_eliminated_products:
            results_test = json.load(products_data_eliminated_products)

        assert insert_products_if_not_in_found_in_data_base(product_tests) == results_test[0]["product_name_fr"]


