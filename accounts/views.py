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

            user = CuA.authenticate(CuA ,username=email, password=password)
            
            if user == None:
                user = CustomUser.objects.create_user(
                    password=password,
                    first_name=first_name,
                    second_name=second_name,
                    email=email
                )
                user.save()
                print(user)
                login(request, user)
            else:
                login(request, user)

            return render(request, 'accounts/thanks.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/create_account.html' , {'form': form})

def login_view(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        while True:        
            username = request.POST['email']
            password = request.POST['password']
            user = CuA.authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                msg = "Bienvenu"
                return render(request, 'accounts/login.html', {'msg':msg})
                
            else:
                # Return an 'invalid login' error message.
                msg = "Compte utilisateur non trouvé!"
                vars_to_template ={
                    'msg':msg,
                    'link':'../create_account',
                    'link_msg': 'Créez un compte utilisateur!'
                }
                
                return render(request,'accounts/login.html', vars_to_template)

    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('home')
