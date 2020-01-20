from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .models import Categories, Product
from users.models import UserCabinet


def get_index(request):
    return render(request, 'main_app/index.html')


def get_categories(request):
    categories = Categories.objects.all()
    user_cabinet = UserCabinet.objects.filter(user__username=request.user.username).first()
    if request.POST:
        if 'subscribe' in request.POST:
            subscribe = Categories.objects.filter(name=request.POST['subscribe']).first()
            user_cabinet.subscriptions.add(subscribe)
            messages.success(request, f"Subscribe to {subscribe.name} was successful")
        elif 'unsubscribe' in request.POST:
            subscribe = Categories.objects.filter(name=request.POST['unsubscribe']).first()
            user_cabinet.subscriptions.remove(subscribe)
            messages.success(request, "Unsubscribe was successful")
    return render(request, "main_app/categories.html", {
        'categories': categories,
        'user_cabinet': user_cabinet
    })


def get_category(request, category_slug):
    category = get_object_or_404(Categories, slug=category_slug)
    products = Product.objects.filter(category=category, relevant__gte=timezone.now())
    if not products:
        messages.warning(request, f'Category "{category}" is empty')
    return render(request, "main_app/category.html", {
        'category': category,
        'products': products
    })
