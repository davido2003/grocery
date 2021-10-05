from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Kitchen, Household
from django.contrib.auth.models import User, auth
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.views.decorators import login_required


def web1(request):
    return render (request, 'index.html')
def web2(request):
    Holds = Household.objects.all()
    return render (request, 'product2.html', {'Holds': Holds})
@login_required(login_url='login')
def web3(request):
    return render (request, 'single2.html')
@login_required(login_url='login')
def web4(request):
    return render (request, 'checkout.html')
@login_required(login_url='login')
def web5(request):
    return render(request, 'help.html')
@login_required(login_url='login')
def web6(request):
    return render(request, 'payment.html')
@login_required(login_url='login')
def web7(request):
    Kitchs = Kitchen.objects.all()
    return render(request, 'product.html',{'Kitchs': Kitchs})
@login_required(login_url='login')
def web8(request):
    return render(request, 'single.html')
@login_required(login_url='login')
def web9(request):
    return render(request, 'terms.html')
@login_required(login_url='login')
def web10(request):
    return render(request, 'contact.html')
@login_required(login_url='login')
def web11(request):
   
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was sucessfully created for ' + user)
                return redirect('login/')
        context = {'form':form}
        return render(request, 'registration.html', context)
def loginpage(request):
    
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username Or Password is Incorrect')
            
    context = {}
    return render(request, 'login.html', context)


def web13(request):
    logout(request)
    return redirect('login')
