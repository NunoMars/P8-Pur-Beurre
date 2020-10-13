import pprint 

def clean_data(file1, file2):
    """
    Clean the downloaded file and choose juste that wee need
    """
    products = file1["products"]  # reach to the list os the products
    wanted_labels = [
        "product_name_fr",
        "url",
        "ingredients_text_fr",
        "nutrition_grade_fr",
        'selected_images']  # list of the labels to search
    print("Faisons du travail de nettoyage sur ", file2, "!")
    processed_products = []

    for product in products:  # the list contains dictionaries
        current_product = {}
        for p_label, p_value in product.items():
            if p_label == "categories":
                current_product.update({"categories": file2})
            if p_label == "_id":
                current_product.update({"product": p_value})
            if p_label == "stores_tags":
                current_product.update({"stores": p_value})

        for p_label, p_value in product.items():  # test if the labels
            if p_label in wanted_labels:
                if len(p_value) != 0:
                    if p_value != " " or p_value != "null":
                        current_product.update({p_label: p_value})
        if len(current_product) == 8:
            if current_product not in processed_products:
                processed_products.append(current_product)
    return processed_products  # return cleaned file


def eliminate_duplicate_products(file):
    """
    Eliminate duplicate products.
    """
    products = file
    print("Faisons du travail de nettoyage!")
    processed_products = []
    for product in products:  # the list contains dictionaries
        if product not in processed_products:
            processed_products.append(product)
    return processed_products  # return cleaned file


def products_to_inser(file):
    """
    Prepare products file to insert to Data-Base.
    """

    products = file  # reach to the list os the products
    wanted_labels = [
        "product",
        "product_name_fr",
        "url",
        "ingredients_text_fr",
        "nutrition_grade_fr",
        ]  # list of the labels to search
    processed_products = []
    for product in products:  # the list contains dictionaries
        current_product = {}
        for p_label, p_value in product.items():
            if p_label in wanted_labels:
                current_product.update({p_label: p_value})
            if p_label == 'selected_images':
                selected = product["selected_images"]
                if len(selected.keys()) == 3:
                    try:
                        product_image_large = selected["front"]["display"]["fr"]
                        current_product.update({"product_image_large": product_image_large})
                        product_image_small = selected["front"]["small"]["fr"]
                        current_product.update({"product_image_small": product_image_small})
                        product_image_nutrition_large = selected["nutrition"]["display"]["fr"]
                        current_product.update({"product_image_nutrition_large": product_image_nutrition_large})
                        product_image_nutrition_small = selected["nutrition"]["small"]["fr"]
                        current_product.update({"product_image_nutrition_small": product_image_nutrition_small})             
                        processed_products.append(current_product)
                    except KeyError:
                        pass
    return processed_products  # return cleaned file


def select_categories(file):
    """
    Search and records all categories for insert in data_base.
    """
    products = file
    current_category = []
    processed_categories = []
    for product in products:
        for p_label, p_value in product.items():
            if p_label == "categories":
                if p_value not in current_category:
                    current_category.append(p_value)
    for item in current_category:
        processed_categories.append({"categorie": item})
    return processed_categories


def select_stores_tags(file):
    """
    Search and records all store_tags for insert in data_base.
    """
    products = file
    pprint.pprint(products)
    current_stores = []
    processed_stores_tags = []
    for product in products:
        for p_label, p_value in product.items():
            if p_label == "stores":
                for value in p_value:
                    if value not in current_stores:
                        current_stores.append(value)
    for item in current_stores:
        processed_stores_tags.append({"stores": item})
    return processed_stores_tags


def select_id_and_stores_tags(file):
    """
    Search and records all id and store_tags for insert in to data_base.
    """
    products = file
    pprint.pprint(products)
    processed_id_and_stores = []
    for product in products:
        print(product["stores"])
        for store in product["stores"]:
            if {'product': product['product'], "stores": store}\
                    not in processed_id_and_stores:
                processed_id_and_stores.append(
                    {'product': product['product'], "stores": store})
    return processed_id_and_stores


def select_id_and_categories(file):
    """
    Search and records all id and categories for insert in to data_base.
    """
    products = file
    processed_id_and_categories = []
    for product in products:
        if {'product': product['product'], "categories": product['categories']}\
                not in processed_id_and_categories:
            processed_id_and_categories.append(
                {'product': product['product'],
                    "categories": product['categories']})
    return processed_id_and_categories
