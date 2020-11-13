from models import Products, History, Categorys
from download_products import DataFiles


print("Debout du travail!...")


DataFiles.download_and_clean_all_products(DataFiles)


products_to_insert = DataFiles.products_to_inser

print(
    "Nous avons ",
    len(products_to_insert),
    "produits téléchargées et nettoyées!",
)


print("Insértion de toutes les categories!")


for data_dict in products_to_insert:
    c = Categorys.objects.get_or_create(category=data_dict["category"])
    p = Products(
        product=data_dict["product"],
        nutrition_grade_fr=data_dict["nutrition_grade_fr"],
        product_name_fr=data_dict["product_name_fr"],
        ingredients_text_fr=data_dict["ingredients_text_fr"],
        product_image_large=data_dict["product_image_large"],
        product_image_small=data_dict["product_image_small"],
        product_image_nutrition_large=data_dict[
            "product_image_nutrition_large"
        ],
        product_image_nutrition_smali=data_dict[
            "product_image_nutrition_small"
        ],
        stores=data_dict["stores"],
        url=data_dict["url"],
    )
    p.save()
    p.category.add(c)


print(
    "Les",
    len(products_to_insert),
    "produits sont, à present, sauvegardées dans la base de données!",
)
