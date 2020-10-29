import random
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import GetProductChoiceForm
from .models import Products


def get_products_choice(request):

    product = request.session.get('product')
    
    product = Products.objects.get(product=product)

    query_set_product = Products.objects.filter(
        category=product.category
        ).filter(
            nutrition_grade_fr=product.nutrition_grade_fr
            ).exclude(product=product.product)    

    random_six_products = random.sample(list(query_set_product), 6)#select 6 products randomly

    if "submit" in request.POST:
        product = request.POST.get("submit")# do something with interview_HTML button is clicked
        request.session['product_to_show'] = product  

        return HttpResponseRedirect('/products/product/')  

    vars_to_template = {
        'proposed_product' : product,
        'products' : random_six_products,     
    }

    return render(request, 'products/products.html', vars_to_template)


def product_view(request):
    product = request.session.get('product_to_show')

    prod = Products.objects.get(product=product)

    vars_to_template = {
                'product_img' : prod.product_image_large,
                'product_name' : prod.product_name_fr,
                'nutriscore' : prod.nutrition_grade_fr,
                'nutrition_img' : prod.product_image_nutrition_large,
                'url' : prod.url,
            } 
    return render(request, 'products/product.html', vars_to_template) 
