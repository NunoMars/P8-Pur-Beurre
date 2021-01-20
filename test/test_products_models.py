from django.test import TestCase
from products.models import Categorys, Products


class CategorysTest(TestCase):


    def setUp(self):
        cat = Categorys.objects.create(
            category="test"
        )
        

    def test_user(self):
        cat = Categorys.objects.get(category="test")
        self.assertEqual(cat.category, "test")



class UserCreationTest(TestCase):


    def setUp(self):
        cat = Categorys.objects.create(
            category="test1"
        )
        p = Products(
            product="123456",
            nutrition_grade_fr= 1,
            product_name_fr="Product",
            ingredients_text_fr="Ingredients",
            product_image_large="Product_img_l",
            product_image_small="Product_img_s",
            product_image_nutrition_large="Product_img_n_l",
            product_image_nutrition_small="Product_img_n_s",
            stores="Stores",
            url="Url",
            )
                
        cat = Categorys.objects.get(category="test1")
        p.category = cat
        p.save()
        

    def test_user(self):
        prod = Products.objects.get(product="123456")
        cat = Categorys.objects.get(category="test1")
        self.assertEqual(prod.product, "123456")
        self.assertEqual(prod.nutrition_grade_fr, 1)
        self.assertEqual(prod.product_name_fr, "Product")
        self.assertEqual(prod.ingredients_text_fr, "Ingredients")
        self.assertEqual(prod.product_image_large, "Product_img_l")
        self.assertEqual(prod.product_image_small, "Product_img_s")
        self.assertEqual(prod.product_image_nutrition_large, "Product_img_n_l")
        self.assertEqual(prod.product_image_nutrition_small, "Product_img_n_s")
        self.assertEqual(prod.stores, "Stores")
        self.assertEqual(prod.category, cat)
        self.assertEqual(prod.url, "Url")
