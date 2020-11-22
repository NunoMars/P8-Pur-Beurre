from django.test import TestCase
from .forms import GetProductChoiceForm, GetProductForm


class GetProductChoiceFormTest(TestCase):

    def test_Cherched_product_field_label(self):
        form = GetProductChoiceForm()
        self.assertTrue(
            form.fields['chosed_product'].label == None or form.fields['chosed_product'].label == 'produit recherché')

class GetProductFormTest(TestCase):
    def test_Cherched_product_field_label(self):
        form = GetProductForm()
        self.assertTrue(
            form.fields['cherched_product'].label == None or form.fields['cherched_product'].label == 'Produit recherché')

    
