from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from categories.models import Categories, EmailSubscribe
from .forms import RegistrationForm, LoginForm


def user_registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successful registration')
            return redirect(reverse('users:login'))
    return render(request, 'users/registration.html', {
        "form": form,
    })


def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request,
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'Successful login')
                if "next" in request.GET:
                    return redirect(request.GET['next'])
                return redirect(reverse('categories:index'))
            messages.warning(request, 'Something wrong!')
    return render(request, 'users/login.html', {
        'form': form,
    })


def user_logout(request):
    logout(request)
    messages.success(request, 'You are logged out')
    return redirect(reverse('users:login'))


@login_required()
def get_cabinet(request):
    categories = Categories.objects.filter(subscribers=request.user).all()
    if request.method == "POST":
        if "send_emails" in request.POST:
            pass

    return render(request, "users/cabinet.html", {
        'categories': categories
    })
