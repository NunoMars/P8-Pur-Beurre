from django.core.management.base import BaseCommand, CommandError
from ...models import Store, Category, Product, History, ProductCategory, ProductStore

from ...download_products import DataFiles
import json


class Command(BaseCommand):

    help = "Insert all products an relations in the models tables."

    print("Debout du travail!...",


    DataFiles.download_and_clean_all_products(DataFiles)
    
    categories = DataFiles.categories

    print(
        "Nous avons, à présent ",
        len(categories),
        "categories!"
        )

    stores_tags = DataFiles.stores_tags

    print(
        "Nous avous aussi ",
        len(stores_tags),
        "magasins!"
        )

    products_to_insert = DataFiles.products_to_inser

    print(
        "Nous avons ",
        len(products_to_insert),
        "produits téléchargées et nettoyées!")

    _id_and_categories = DataFiles._id_and_categories

    print(len(
        _id_and_categories),
        "Les identifiants et les catégories sont prêts à être insérés."
        )

    _id_and_stores = DataFiles._id_and_stores

    print(len(
        _id_and_stores),
        "Les identifiants et les magasins sont prêts à être insérés."
        )

    print("Insértion de tous les nouveaux produits!")

    for data_dict in categories:
        try:
            data_dict = Category(categorie=data_dict)
            data_dict.save()
        except:
            pass
    print("Insértion de Categories terminé!")

    for data_dict in stores_tags:
        try:
            data_dict = Store(store=data_dict)
            data_dict.save()
        except:
            pass
    print("Insértion de Magasins terminé!")

    for data_dict in products_to_insert:
        try:
            data_dict = Product(**data_dict)
            data_dict.save()
        except:
            pass
    print("Insértion des Produits terminé!")

    for data_dict in _id_and_categories:
        try:
            data_dict = ProductCategory(**data_dict)
            data_dict.save()
        except:
            pass
    print("Insértion de Categories de Produits terminé!")

    for data_dict in _id_and_stores:
        try:
            data_dict = ProductStore(**data_dict)
            data_dict.save()
        except:
            pass
    print("Insértion des magasins por chaque produit terminé!")

    print("Les produits sont, à present,",
        " sauvegardées dans la base de données!")


