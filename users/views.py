from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import RegistrationForm


def user_registration(request):
    user_form = RegistrationForm()
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Successful registration')
            return redirect(reverse('users:login'))
    return render(request, 'users/registration.html', {
        "user_form": user_form,
    })


def user_login(request):
    return render(request, 'users/login.html')
