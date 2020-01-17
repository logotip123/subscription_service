from django.shortcuts import render

from .models import Categories


def get_index(request):
    return render(request, 'main_app/index.html')

def get_categories(request):
    categories = Categories.objects.all()
    return render(request, "main_app/categories.html", {
        'categories': categories
    })
