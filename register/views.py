from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("register:signin")

    context = {'form': form}

    return render(request, 'register/register.html', context)


def loginpage(request):
    if request.method == 'POST':
        __username = request.POST.get('username')
        __password = request.POST.get('password')
        user = authenticate(username=__username, password=__password)
        if user is not None:
            login(request, user)
            return redirect('polls:index')
        else:
            messages.warning(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'register/SignIn.html', context)


@login_required
def logout_user(request):
    logout(request)
    context = {}
    return render(request, 'polls/index.html')
