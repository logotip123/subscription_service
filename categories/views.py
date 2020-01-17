from django.shortcuts import render

from .models import Categories


def get_categories(request):
    categories = Categories.objects.all()
    return render(request, "categories/index.html", {
        'categories': categories
    })
