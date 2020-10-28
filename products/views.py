import random
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import GetProductChoiceForm
from .models import Products, ProductForm, ProductChosed


def get_products_choice(request):
    ProductChosed.objects.all().delete()

    req = ProductForm.objects.filter().latest('cherched_product')#Last form entry
    product_to_query = req.cherched_product
    req_proposed_product = Products.objects.get(product=product_to_query)#product recherched by costumer


    query_set_product = Products.objects.filter(
        category=req_proposed_product.category
        ).filter(
            nutrition_grade_fr=req_proposed_product.nutrition_grade_fr
            ).exclude(product=req_proposed_product.product)[:6]    

    """random_items = random.sample(list(query_set_product), 6)#select 6 products randomly"""
    prod1 = query_set_product[0]
    prod2 = query_set_product[1]
    prod3 = query_set_product[2]
    prod4 = query_set_product[3]
    prod5 = query_set_product[4]
    prod6 = query_set_product[5]

    if "submit" in request.POST:
        if "P1 choisi" == request.POST.get("submit"):# do something with interview_HTML button is clicked
            prod = ProductChosed(
                proposed_product=prod1.product
                )
  
       
        elif "P2 choisi" == request.POST.get("submit"):
            prod = ProductChosed(
                proposed_product=prod2.product
                )

        elif "P3 choisi" == request.POST.get("submit"):
            prod = ProductChosed(
                proposed_product=prod3.product
                )

        elif "P4 choisi" == request.POST.get("submit"):
            prod = ProductChosed(
                proposed_product=prod4.product
                )

        elif "P5 choisi" == request.POST.get("submit"):
            prod = ProductChosed(
                proposed_product=prod5.product
                )

        elif "P6 choisi" == request.POST.get("submit"):
            prod = ProductChosed(
                proposed_product=prod6.product
                )

        prod.save()
        return HttpResponseRedirect('/product/')  

    vars_to_template = {
        'product_img' : req_proposed_product.product_image_large,
        'product_name' : req_proposed_product.product_name_fr,
        'product_img_choice_1' : prod1.product_image_large,
        'product_name_choice_1' : prod1.product_name_fr,
        'product_nut_choice_1' : prod1.nutrition_grade_fr,
        'product_img_choice_2' : prod2.product_image_large,
        'product_name_choice_2' : prod2.product_name_fr,
        'product_nut_choice_2' : prod2.nutrition_grade_fr,
        'product_img_choice_3' : prod3.product_image_large,
        'product_name_choice_3' : prod3.product_name_fr,
        'product_nut_choice_3' : prod3.nutrition_grade_fr,
        'product_img_choice_4' : prod4.product_image_large,
        'product_name_choice_4' : prod4.product_name_fr,
        'product_nut_choice_4' : prod4.nutrition_grade_fr,
        'product_img_choice_5' : prod5.product_image_large,
        'product_name_choice_5' : prod5.product_name_fr,
        'product_nut_choice_5' : prod5.nutrition_grade_fr,
        'product_img_choice_6' : prod6.product_image_large,
        'product_name_choice_6' : prod6.product_name_fr,
        'product_nut_choice_6' : prod6.nutrition_grade_fr,        
    }

    return render(request, 'products/products.html', vars_to_template)


@login_required(login_url='/login/')
def product_view(request):
    req = ProductChosed.objects.filter().latest('proposed_product')
    product_to_query = req.proposed_product

    prod = Products.objects.get(product=product_to_query)

    vars_to_template = {
                'product_img' : prod.product_image_large,
                'product_name' : prod.product_name_fr,
                'nutriscore' : prod.nutrition_grade_fr,
                'nutrition_img' : prod.product_image_nutrition_large,
                'url' : prod.url,
            } 
    return render(request, 'products/product.html', vars_to_template) 
