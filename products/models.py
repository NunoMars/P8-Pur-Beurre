from django.db import models

class Store(models.Model):
    """ Class to define the Store table."""
    stores_tags = models.CharField(primary_key=True)

    class Meta:
        db_table = 'store'


class Category(models.Model):
    """ Class to define the Category table."""
    categories = models.CharField(primary_key=True)

    class Meta:
        db_table = 'category'


class Product(models.Model):
    """ Class to define the Product table."""
    _id = models.CharField(primary_key=True)
    repères_nutritionnelles_100g  = models.TextField()
    nutrition_grade_fr = models.CharField(max_length=1)
    product_name_fr = models.TextField()
    image_url = models.URLField()
    url = models.URLField()

    class Meta:
        db_table = 'product'


class History(models.Model):
    """ Class to define the History table."""
    id = models.ForeignKey("User", on_delete=models.CASCADE)
    chosen_product = models.ForeignKey(
        "Product", related_name='chosen_product ', on_delete=models.CASCADE)
    remplacement_product = models.ForeignKey(
        "Product", related_name='remplacement_product', on_delete=models.CASCADE)

    class Meta:
        db_table = 'history'


class ProductCategory(models.Model):
    """ Class to define the Product category table."""
    _id = models.ForeignKey("Product", on_delete=models.CASCADE)
    categories = models.ForeignKey("Category", on_delete=models.CASCADE)

    class Meta:
        primary_key = (('_id', 'categories'),)
        db_table = 'product_category'


class ProductStore(models.Model):
    """ Class to define the Product Store table."""
    _id = models.ForeignKey("Product", on_delete=models.CASCADE)
    stores_tags = models.ForeignKey(Store, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('_id', 'stores_tags'),)
        db_table = 'product_store'
