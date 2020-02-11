from django.db import models


class User(models.Models):
    """ Class to define the User table."""
    name = models.CharField("nom", max_length=200, unique=True)
    password = models.CharField("password", max_length=200)
    email = models.EmailField("email", max_length=100)

    class Meta:
        verbose_name = 'utilisateur'
    def __str__(self):
        return self.name


class Store(models.Models):
    """ Class to define the Store table."""
    store = models.CharField("magasin", max_length=100, primary_key=True)

    class Meta:
        verbose_name = 'magasin'
    def __str__(self):
        return self.store


class Category(models.Models):
    """ Class to define the Category table."""
    category = models.CharField('catégorie', max_length=200 ,primary_key=True)

    class Meta:
        verbose_name = 'catégorie'
    def __str__(self):
        return self.category


class Product(models.Models):
    """ Class to define the Product table."""
    _id = models.IntegerField("référence", primary_key=True)
    ingredients_text_fr = models.TextField("Ingrédients", )
    nutrition_grade_fr = models.CharField("Nutrition grade", max_length=1)
    product_name_fr = models.TextField("Nom du produit", )
    url = models.TextField('Url du produit sur Openfoodfacts', )
    picture = models.TextField("Url de l'image", )
    store = models.ManyToManyField(Store, related_name='produits', )
    category = models.ManyToManyField(Category, related_name='catégories')

    class Meta:
        verbose_name = 'produit'
    def __str__(self):
        return self.product_name_fr


class History(models.Models):
    """ Class to define the History table."""
    id = models.ForeignKeyField(User, backref='history', on_delete=models.CASCADE)
    chosen_product = models.ForeignKeyField(
        Product, related_name='produit choisi', backref='history')
    remplacement_product = models.ForeignKeyField(
        Product, related_name='produit proposé', backref='history')

    class Meta:
        verbose_name = 'historique de produits'

