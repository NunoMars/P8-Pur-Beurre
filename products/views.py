from django.http import HttpResponseRedirect
from django.shortcuts import render
from home.forms import GetProductForm
from .models import Products, ProductForm

def get_products_choice(request):

    req = ProductForm.objects.filter().latest('cherched_product')
    product_to_query = req.cherched_product
    req_proposed_product = Products.objects.get(product=product_to_query)

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
    vars_to_template = {
        'product_img' : req_proposed_product.product_image_large,
        'product_name' : req_proposed_product.product_name_fr
    }
    return render(request, 'products/products.html', vars_to_template)

