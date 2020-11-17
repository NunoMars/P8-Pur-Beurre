from django.test import TestCase
from django.urls import reverse

from .models import Products, Categorys
from accounts.models import CustomUser, History

class IndexPageTest(TestCase):
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class SearchPageTest(TestCase):
    def test_search_page(self):
        response = self.client.get(reverse('search_product'))
        self.assertEqual(response.status_code, 200)


class MentionsLegalesPageTestCase(TestCase):
    def test_mentions_legales_page(self):
        response = self.client.get(reverse('mentions_legales'))
        self.assertEqual(response.status_code, 200)

class AllDbTests(TestCase):

    def setUp(self):

        i = 1
        while i <= 20:
            c = Categorys(
                category="category",
            )
            c.save()

            p = Products(
                product="123456"+str(i),
                nutrition_grade_fr="T",
                product_name_fr="Product"+str(i),
                ingredients_text_fr="Ingredients"+str(i),
                product_image_large="Product_img_l"+str(i),
                product_image_small="Product_img_s"+str(i),
                product_image_nutrition_large="Product_img_n_l"+str(i),
                product_image_nutrition_small="Product_img_n_s"+str(i),
                stores="Stores"+str(i),
                url="Url"+str(i),
                )
            
            cat = Categorys.objects.get(category="category")
            p.category = cat
            p.save()
            i += 1
        
        user = CustomUser.objects.create(
            email="email@email.com",
            first_name="first_name",
            second_name="second_name",
            password="12345678"
        )

        user = CustomUser.objects.get(email=user)
        chosen_product = Products.objects.get(product="1234561")
        remplacement_product=Products.objects.get(product="1234562")

        history = History.objects.create(
            user=user,
            chosen_product=chosen_product,
            remplacement_product=remplacement_product
        )

    def test_product_view_page(self):
        product = Products.objects.get(product="1234561").product

        response = self.client.get(reverse('product_detail', args=(product,)))
        self.assertEqual(response.status_code, 200)

    def test_products_list_page(self):

        product = Products.objects.get(product="1234561").product

        response = self.client.get(reverse('products_list', args=(product,)))
        self.assertEqual(response.status_code, 200)


    def test_history_page(self):
        response = self.client.get(reverse('history'))
        self.assertEqual(response.status_code, 302)


