from django.http import HttpResponseRedirect
from django.shortcuts import render
from products.models import Products
from .forms import GetProductForm

def get_product(request):
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
                        product_name_fr__contains=cherched_product
                        )[:1]
                    product = req[0]
                    request.session['product'] = product.product                    

                except:
                    error = "Erreur!! Impossible de trouver le produit recherché! essayez encore."
                    vars_to_template={
                       'form': form,
                       'atention': error 
                    }
                    
                    return render(request, 'home/home.html', vars_to_template)
                
                # redirect to a new URL:
                return HttpResponseRedirect('/products/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GetProductForm()

    return render(request, 'home/home.html', {'form': form})
