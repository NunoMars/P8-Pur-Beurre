from django.db import models


class Categorys(models.Model):
    category = models.CharField(primary_key=True, max_length=50)

    class Meta:
        db_table = "categorys"


class Products(models.Model):
    """ Class to define the Product table. I used TextField because the lenght is superior than 200, and url field is biger"""

    product = models.CharField(max_length=20, primary_key=True)
    nutrition_grade_fr = models.IntegerField()
    product_name_fr = models.TextField()
    ingredients_text_fr = models.TextField()
    product_image_large = models.TextField()
    product_image_small = models.TextField()
    product_image_nutrition_large = models.TextField()
    product_image_nutrition_small = models.TextField()
    url = models.TextField()
    stores = models.TextField()
    category = models.ForeignKey(
        "Categorys", on_delete=models.CASCADE, default="category"
    )

    class Meta:
        db_table = "products"
