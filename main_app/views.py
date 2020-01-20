from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from .models import Categories, Product


def get_index(request):
    return render(request, 'main_app/index.html')


def get_categories(request):
    categories = Categories.objects.all()
    return render(request, "main_app/categories.html", {
        'categories': categories
    })


def get_category(request, category_slug):
    category = get_object_or_404(Categories, slug=category_slug)
    products = Product.objects.filter(category=category).all()
    if not products:
        messages.warning(request, f'Category "{category}" is empty')
    return render(request, "main_app/category.html", {
        'category': category,
        'products': products
    })
