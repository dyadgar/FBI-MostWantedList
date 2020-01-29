from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import RegisterForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {'form': form})


def home(request):
    count = User.objects.count()
    return render(request,'profile_app/home.html',{
        'count':count
    })


def profile(request,username='Default Username'):
    return render(request,'profile_app/profile.html')


