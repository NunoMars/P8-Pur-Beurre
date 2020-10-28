from django.shortcuts import render, redirect

from django.contrib.auth import logout

def login_view(request):
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('home')
