import random
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import GetProductChoiceForm, GetProductForm
from .models import Products, History

from accounts.models import CustomUser
from django.contrib.auth.models import User

def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        while True:
            form = GetProductForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                cherched_product = form.cleaned_data['cherched_product']

                try:
                    req = Products.objects.filter(
                        product_name_fr__icontains=cherched_product
                        )[:1]
                    product = req[0]
                    print(product.product)
                    request.session['product'] = product.product             
                    
                except:
                    not_found = "Impossible de trouver le produit recherché! Essayez encore."
                    context={
                       'form': form,
                       'atention': not_found 
                    }
                    
                    return render(request, 'products/index.html', context)
                
                # redirect to a new URL:
                return HttpResponseRedirect('/products/product')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GetProductForm()
        context = {
            'form': form
        }

    return render(request, 'products/index.html', context)


def get_user_choice(request, product_found):
    product = Products.objects.get(product=product_found)

    context = {
        "proposed_product": product
    }
    return render(request, 'products/product_found.html', context)

def get_products_choice(request, product):    

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

        save = History(User, chosen_product=product_to_show, remplacement_product=save_product)
        save.save()        

        return HttpResponseRedirect('/products/product/')  

    context = {
        'proposed_product' : product,
        'products' : random_six_products,     
    }

    return render(request, 'products/products.html', context)


def product_view(request, product):
    
    product = Products.objects.get(product=str(product))

    context = {
                'product' : product,
            }
    
    return render(request, 'products/product.html', context) 

def history(request):
    return render(request, 'products/history.html')