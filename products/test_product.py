import json
import requests
import pprint as pp
import clear_data


def start():

    r = requests.get(
                    "https://fr.openfoodfacts.org/cgi/search.pl?action=process&tagtype_0=categories&tag_contains_0=contains&tag_0=" +
                    "snacks" + "&tagtype_1=categories&tag_contains_1=contains&tag_1=" +
                    "snacks" + "&sort_by=unique_scans_n&page_size=1&axis_x=energy&axis_y=products_n&action=process&page=2&json=1"
                    )
                    
    current_product = json.loads(r.content)
    with open('data.json', 'w') as fp:
        json.dump(current_product, fp)
    select= current_product["products"][1]
    product_image_large = select["selected_images"]["front"]["display"]["fr"]
    product_image_small = select["selected_images"]["front"]["small"]["fr"]
    product_image_nutrition_large = select["selected_images"]["nutrition"]["display"]["fr"]
    product_image_nutrition_small = select["selected_images"]["nutrition"]["small"]["fr"]
    pp.pprint(select)
    print(product_image_large)
    print(product_image_nutrition_large)

    product=clear_data.clean_data(current_product, "snacks")
    pp.pprint(product)

if __name__ == "__main__":
    start()

