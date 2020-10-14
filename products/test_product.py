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
    product0=clear_data.clean_data(current_product, "snacks")
    pp.pprint(product0)

    selected = product0
    pp.pprint(selected)   


if __name__ == "__main__":
    start()

