import requests
import json

from .clear_data import clean_data
from .models import Products, Categorys



def insert_products_if_not_in_found_in_data_base(product):
    """ 
    If the cherched product is not found in apps database,
    it request 10 new products on openfoodfacts web site,
    clean the data, insert all requested products in apps database
    """ 

    r = requests.get(
                    "https://fr.openfoodfacts.org/cgi/search.pl?action=process&search_terms="
                    + product +
                    "&sort_by=unique_scans_n&page_size=10&json=1"
                )

    products = json.loads(r.content)

    processed_categories = []
    products_list = products["products"]
    for product in products_list:
        for p_label, p_value in product.items():
            if p_label == "categories":
                categories = p_value.split(',')
                for item in categories:
                    if item not in processed_categories:
                        processed_categories.append(item)

    cleaned_products = clean_data(products, processed_categories[0])

    #insert the products in database
    for data_dict in cleaned_products:
        try:
            c = Categorys(category=data_dict["category"])
            c.save()

            if data_dict["nutrition_grade_fr"] == "a":
                nut = 1
            if data_dict["nutrition_grade_fr"] == "b":
                nut = 2
            if data_dict["nutrition_grade_fr"] == "c":
                nut = 3
            if data_dict["nutrition_grade_fr"] == "d":
                nut = 4
            if data_dict["nutrition_grade_fr"] == "e":
                nut = 5

            p = Products(
                product=str(data_dict["product"]),
                nutrition_grade_fr=nut,
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
            pass