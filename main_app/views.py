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
    if request.POST:
        if 'subscribe' in request.POST:
            category = Categories.objects.filter(name=request.POST['subscribe']).first()
            request.user.user_cabinet.subscriptions.add(category)
            messages.success(request, f"Subscribe to {category.name} was successful")
        elif 'unsubscribe' in request.POST:
            category = Categories.objects.filter(name=request.POST['unsubscribe']).first()
            request.user.user_cabinet.subscriptions.remove(category)
            messages.success(request, "Unsubscribe was successful")
        else:
            pass
    return render(request, "main_app/categories.html", {
        'categories': categories,
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
