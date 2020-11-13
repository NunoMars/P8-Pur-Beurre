from django.core.management.base import BaseCommand, CommandError

from products.models import Products, History, Categorys
from products.download_products import DataFiles


class Command(BaseCommand):
    def handle(self, *args, **options):

        help = "Insert all products an relations in the models tables."

        print("Debout du travail!...")

        DataFiles.download_and_clean_all_products(DataFiles)

        products_to_insert = DataFiles.products_to_inser

        print(
            "Nous avons ",
            len(products_to_insert),
            "produits téléchargées et nettoyées!",
        )

        print("Insértion de tous les produits dans la base de données!")

        try:
            for data_dict in products_to_insert:
                c = Categorys(category=data_dict["category"])
                c.save()

                p = Products(
                    product=str(data_dict["product"]),
                    nutrition_grade_fr=data_dict["nutrition_grade_fr"],
                    product_name_fr=data_dict["product_name_fr"],
                    ingredients_text_fr=data_dict["ingredients_text_fr"],
                    product_image_large=data_dict["product_image_large"],
                    product_image_small=data_dict["product_image_small"],
                    product_image_nutrition_large=data_dict[
                        "product_image_nutrition_large"
                    ],
                    product_image_nutrition_small=data_dict[
                        "product_image_nutrition_small"
                    ],
                    stores=data_dict["stores"],
                    url=data_dict["url"],
                )

                cat = Categorys.objects.get(category=data_dict["category"])
                p.category = cat
                p.save()

        except:
            raise CommandError(
                "Ups une erreur est arrivé, insertion aborté!! sur le produit",
                p.product_name_fr,
            )

        self.stdout.write(
            self.style.SUCCESS(
                "Les produits sont, à present, sauvegardées dans la base de données!"
            )
        )
