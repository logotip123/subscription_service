from django.contrib import messages
from django.shortcuts import render, redirect
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
    products = Product.objects.filter(category__slug=category_slug).all()
    try:
        category = products[0].category.name
    except IndexError:
        messages.warning(request, f'Category "{category_slug}" does not exist or empty')
        return redirect(reverse('main_app:categories'))
    return render(request, "main_app/category.html", {
        'products': products,
        'category': category
    })
