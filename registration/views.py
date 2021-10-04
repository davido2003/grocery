from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
# Create your views here.
def web11(request):

    if request.method == 'POST':
        first_name == request.POST['first_name']
        username == request.POST['username']
        last_name == request.POST['last_name']
        email == request.POST['email']
        password1 == request.POST['password1']
        password2 == request.POST['password2']

        user = User.objects.create_user(username=username ,first_name=first_name, last_name=last_name, email=email, password1=password)
        user.save();
        print('user created')
        return redirect('/')
    else:
        return render(request, 'registration.html')