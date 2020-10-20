

from django.http import HttpResponseRedirect
from django.shortcuts import render
from home.forms import GetProductForm
from .models import Products, ProductForm

def get_products_choice(request):

    p = ProductForm.objects.filter().latest('cherched_product')
    product = p.cherched_product
    print(product)
    req = Products.objects.get(product=product)
    product_img = req.product_image_large
    product_name = req.product_name_fr
    """# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GetProductForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            cherched_product = form.cleaned_data['cherched_product']
            print(cherched_product)
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/products/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GetProductForm()"""

    return render(request, 'products/products.html')

