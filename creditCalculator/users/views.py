

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages, auth
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm


def registration(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Поздравляю {request.POST.get("username")}! Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f'{request.POST.get("username")}, Вы успешно авторизовались!')
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()

    return render(request, 'users/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.warning(request, 'Вы вышли из аккаунта!')
    return HttpResponseRedirect(reverse('home'))
