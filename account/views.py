from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from company.models import Company

from .forms import SignUpForm

# Create your views here.
def register_user(request):
    companys = Company.objects.order_by('id')[:1]

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('pipeline')
    else:
        form = SignUpForm()
        return render(request, 'signup.html', {'form':form, 'companys':companys})

    return render(request, 'signup.html', {'form':form, 'companys':companys})


def login_user(request):
    companys = Company.objects.order_by('id')[:1]

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect('pipeline')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('login')
    else:
        return render(request, 'login.html', {'companys': companys})

def logout_user(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('login')