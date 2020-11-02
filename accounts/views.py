from django.shortcuts import render, redirect
from django.contrib.auth import logout, login
from products.models import Products
from .backend import CustomUserAuth as CuA
from .forms import CustomUserCreationForm
from .models import CustomUser

def create_account_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']           
            first_name = form.cleaned_data['first_name']
            second_name = form.cleaned_data['second_name']
            password = form.clean_password2

            user = CuA.autenthicate(CuA ,username=email, password=password)
            if user == None:
                user = CustomUser(
                    password=password,
                    first_name=first_name,
                    second_name=second_name,
                    email=email
                )
                user.save()
                login(request, user)
            else:
                login(request, user)

            return render(request, 'accounts/thanks.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/create_account.html' , {'form': form})

def login_view(request):

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('home')
