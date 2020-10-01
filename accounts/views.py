from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
from .forms import CreateUserForm
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group


@unauthenticated_user
def registerPage(request):

    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)

            messages.success(request, 'Cuenta creada para' + username)
            return redirect('login')
    context = {'form': form}
    return render(request, "accounts/register.html", context)


@unauthenticated_user
def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Su usuario o contraseña son incorrectos')

    return render(request, "accounts/login.html")


def logoutUser(request):
    logout(request)
    return redirect('login')