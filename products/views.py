import random
from django.utils.html import escape
from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import GetProductChoiceForm, GetProductForm
from .models import Products
from accounts.models import CustomUser, History
from django.contrib.auth.models import User
from .new_functionality import insert_products_if_not_in_found_in_data_base


def index(request):
    """
    Show the index template.
    """

    return render(request, "products/index.html")


def search(request):
    """
    Fonction to search one product in data base.
    """
    # en, copier sur celinelever formulaire django et ecrire le mien
    query = request.GET.get("query")
    # Query Html escape
    user_product = escape(query)
    if not query:
        context = {"attention": "Vous devez renseigner un produit!!"}
        return render(request, "products/index.html", context)

    else:
        # Product contains the query is and query is not sensitive to case.
        product = Products.objects.filter(product_name_fr__icontains=user_product)[:1]

        if not product.exists():
            try:
                new_product = insert_products_if_not_in_found_in_data_base(user_product)#new_feature
                product = Products.objects.filter(product_name_fr__icontains=new_product)[:1]

                return redirect("products_list", product=product[0].product)
            except:
                context = {
                    "attention": "Produit non trouvé, essayer de chercher un autre produit svp!!"
                }
            return render(request, "products/index.html", context)
        else:
            product = product[0]

            return redirect("products_list", product=product.product)

    return render(request, "products/search_product.html", context)


def products_list(request, product):
    """
    It shows the recherched product name and image, generates one list
    randomly of 6 products, and save the products selected
    by the user if he is loged in.
    """
    product_found = get_object_or_404(Products, product=product)

    nut = product_found.nutrition_grade_fr

    query_set_product = (
        Products.objects.filter(category=product_found.category)
        .filter(
            Q(nutrition_grade_fr__lte=nut) 
        )  # propose products with value less or equal at the search product
        .exclude(product=product_found.product)
    )

    if len(query_set_product) >= 6:
        random_six_products = random.sample(
            list(query_set_product), 6
        )  # select 6 products randomly
    
    else:
        query_set_product = Products.objects.filter(
            Q(nutrition_grade_fr__lte=nut) 
        ).exclude(product=product_found.product)

        random_six_products = random.sample(
            list(query_set_product), 6
        )  # select 6 products randomly   


    if "submit" in request.POST:  # do something with interview_HTML button is clicked
        save_product = request.POST.get("submit")
        save_product = Products.objects.get(product=save_product)
        if not request.user.is_authenticated:
            return redirect("%s?next=%s" % (settings.LOGIN_URL, request.path))
        user = request.user

        user = CustomUser.objects.get(email=user)

        save = History(
            user=user,
            chosen_product=product_found,
            remplacement_product=save_product,
        )
        save.save()

    context = {
        "proposed_product": product_found,
        "products": random_six_products,
    }

    return render(request, "products/products.html", context)


def product_view(request, product):
    """Show the product details wen clic on."""
    product = Products.objects.get(product=product)

    context = {
        "product": product,
    }

    return render(request, "products/product_detail.html", context)


@login_required()
def history(request):
    """Fonction for show the products,
    tha are chosed by the user, login required."""
    user = request.user
    user = CustomUser.objects.get(email=user)

    get_user_history = History.objects.filter(user=user)
    products_list = []
    for item in get_user_history:
        chosen_product = item.chosen_product
        products_list.append(chosen_product)
        remplacement_product = item.remplacement_product
        products_list.append(remplacement_product)

    context = {
        "user": user,
        "list_of_products": products_list,
    }
    return render(request, "products/history.html", context)


def mentions_legales(request):
    """
    Show the 'legal mentions'!
    """

    return render(request, "products/mentions_legales.html")


def contact(request):
    """
    Show the 'contact'!
    """

    return render(request, "contact.html")
