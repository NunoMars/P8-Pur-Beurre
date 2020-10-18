from django.http import HttpResponseRedirect
from django.shortcuts import render
"""from django.template import RequestContext"""

from .forms import GetProductForm

def get_product(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GetProductForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/merci/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GetProductForm()

    return render(request, 'home/home.html', {'form': form})
    """return render('pur_beurre/base.html', {'form': form},  RequestContext(request))"""
# Added RequestContext
    """alouer passage methode POST"""

# Create your views here.
