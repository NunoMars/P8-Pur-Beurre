import random
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import GetProductChoiceForm
from .models import Products, ProductForm

def get_products_choice(request):

    req = ProductForm.objects.filter().latest('cherched_product')#Last form entry
    product_to_query = req.cherched_product
    req_proposed_product = Products.objects.get(product=product_to_query)#product recherched by costumer


    query_set_product = Products.objects.filter(category=req_proposed_product.category)    

    random_items = random.sample(list(query_set_product), 6)#select 6 products randomly
    prod1 = random_items[0]
    prod2 = random_items[1]
    prod3 = random_items[2]
    prod4 = random_items[3]
    prod5 = random_items[4]
    prod6 = random_items[5]

    if "choice_boutton" in request.POST:
        if "P1 choisi" == request.POST.get("choice_boutton"):
            print("vous avez chois le produit 1") 
        # do something with interview_HTML button is clicked
        elif "P2 choisi" == request.POST.get("choice_boutton"):
            print("vous avez chois le produit 2")
        elif "P3 choisi" == request.POST.get("choice_boutton"):
            print("vous avez chois le produit 3")
            # do something with interview_CSS button is clicked

    vars_to_template = {
        'product_img' : req_proposed_product.product_image_large,
        'product_name' : req_proposed_product.product_name_fr,
        'product_img_choice_1' : prod1.product_image_large,
        'product_name_choice_1' : prod1.product_name_fr,
        'product_img_choice_2' : prod2.product_image_large,
        'product_name_choice_2' : prod2.product_name_fr,
        'product_img_choice_3' : prod3.product_image_large,
        'product_name_choice_3' : prod3.product_name_fr,
        'product_img_choice_4' : prod4.product_image_large,
        'product_name_choice_4' : prod4.product_name_fr,
        'product_img_choice_5' : prod5.product_image_large,
        'product_name_choice_5' : prod5.product_name_fr,
        'product_img_choice_6' : prod6.product_image_large,
        'product_name_choice_6' : prod6.product_name_fr,
        
    }
    return render(request, 'products/products.html', vars_to_template)

