from django.db import models
from django.contrib.auth.models import User

class Products(models.Model):
    """ Class to define the Product table."""
    product = models.CharField(primary_key=True, max_length=50)
    nutrition_grade_fr = models.CharField(max_length=1)
    product_name_fr = models.TextField()
    ingredients_text_fr = models.TextField()
    product_image_large = models.TextField()
    product_image_small = models.TextField()
    product_image_nutrition_large = models.TextField()
    product_image_nutrition_small = models.TextField()
    url = models.TextField()
    stores = models.TextField()
    category = models.ManyToManyField("Categorys")
    class Meta:
        db_table = 'products'

class Categorys(models.Model):
    category = models.CharField(primary_key=True, max_length=50)
    class Meta:
        db_table = 'categorys'


class History(models.Model):
    """ Class to define the History table."""
    User.username = models.ForeignKey("User", on_delete=models.CASCADE)
    chosen_product = models.ForeignKey(
        "Products", related_name='chosen_product', on_delete=models.CASCADE)
    remplacement_product = models.ForeignKey(
        "Products", related_name='remplacement_product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'history'

class ProductForm(models.Model):
    cherched_product = models.CharField(primary_key=True, max_length=50)



