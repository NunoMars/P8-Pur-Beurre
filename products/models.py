from django.db import models
from django.contrib.auth.models import User

class Store(models.Model):
    """ Class to define the Store table."""
    stores = models.CharField(primary_key=True, max_length=100)

    class Meta:
        db_table = 'store'


class Category(models.Model):
    """ Class to define the Category table."""
    categorie = models.CharField(primary_key=True, max_length=40)

    class Meta:
        db_table = 'category'


class Product(models.Model):
    """ Class to define the Product table."""
    product = models.CharField(primary_key=True, max_length=20)
    repères_nutritionnelles_100g  = models.TextField()
    nutrition_grade_fr = models.CharField(max_length=1)
    product_name_fr = models.TextField()
    ingredients_text_fr = models.TextField()
    product_image_large = models.TextField()
    product_image_small = models.TextField()
    product_image_nutrition_large = models.TextField()
    product_image_nutrition_small = models.TextField()
    url = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'


class History(models.Model):
    """ Class to define the History table."""
    User.username = models.ForeignKey("User", on_delete=models.CASCADE)
    chosen_product = models.ForeignKey(
        "Product", related_name='chosen_product', on_delete=models.CASCADE)
    remplacement_product = models.ForeignKey(
        "Product", related_name='remplacement_product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'history'


class ProductCategory(models.Model):
    """ Class to define the Product category table."""
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    categorie = models.ForeignKey("Category", on_delete=models.CASCADE)

    class Meta:
        unique_together = (('product', 'categorie'),)
        db_table = 'product_category'


class ProductStore(models.Model):
    """ Class to define the Product Store table."""
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('product', 'store'),)
        db_table = 'product_store'
