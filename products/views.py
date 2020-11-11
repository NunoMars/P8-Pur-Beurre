import random
from django.utils.html import escape
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import GetProductChoiceForm, GetProductForm
from .models import Products, History
from accounts.models import CustomUser
from django.contrib.auth.models import User

def index(request):

    return render(request, 'products/index.html')

def search(request):
    #en, copier sur celinelever formulaire django et ecrire le mien
    query = request.GET.get('query')
    #Query Html escape
    user_product = escape(query)
    if not query:
        context = {
            'attention': "Vous devez renseigner un produit!!"
            }
        return render(request, 'products/index.html', context)

    else:       
        # Product contains the query is and query is not sensitive to case.
        product = Products.objects.filter(
            product_name_fr__icontains=user_product
            )[:1]

        if not product.exists():
            context = {
            'attention': "Produit non trouvé, essayer de chercher un autre produit svp!!"
            }
            return render(request, 'products/index.html', context)
        else:
            product=product[0]

            return redirect('products_list', product=product.product)

    return render(request, 'products/search_product.html', context)

def products_list(request, product):    
    product = get_object_or_404(Products, product=product)

    query_set_product = Products.objects.filter(
        category=product.category
        ).filter(
            nutrition_grade_fr=product.nutrition_grade_fr
            ).exclude(product=product.product)    

    random_six_products = random.sample(list(query_set_product), 6)#select 6 products randomly

    if "submit" in request.POST:
        product = request.POST.get("submit")# do something with interview_HTML button is clicked
        save_product = request.POST.get("submit")
        if not request.user.is_authenticated:
            return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))    

        save = History(User, chosen_product=product.product, remplacement_product=save_product)
        save.save()        

        return HttpResponseRedirect('/products/product/')  

    context = {
        'proposed_product' : product,
        'products' : random_six_products,     
    }

    return render(request, 'products/products.html', context)


def product_view(request, product):
    
    product = Products.objects.get(product=product)
    print(product)
    context = {
                'product' : product,
            }
    
    return render(request, 'products/product_detail.html', context)


def history(request):
    return render(request, 'products/history.html')