from django.core.management.base import BaseCommand, CommandError

from products.models import Products, History
from products.download_products import DataFiles
import json


class Command(BaseCommand):


    def handle(self, *args, **options):

        help = "Insert all products an relations in the models tables."

        print("Debout du travail!...")


        DataFiles.download_and_clean_all_products(DataFiles)
        

        products_to_insert = DataFiles.products_to_inser

        print(
            "Nous avons ",
            len(products_to_insert),
            "produits téléchargées et nettoyées!")



        print("Insértion de tous les nouveaux produits!")
        
        for data_dict in products_to_insert:
            try:
                data = Products(**data_dict)
                data.save()
                
            except:
                raise CommandError("Ups, il y a eu une erreur dans l'insertion, commande aborté!!")
            
        self.stdout.write(self.style.SUCCESS("Les produits sont, à present, sauvegardées dans la base de données!"))