from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone

from .models import Categories, EmailSubscribe, Product
from .forms import SearchForm


def get_index(request):
    return render(request, 'categories/index.html')


def get_categories(request):
    categories = Categories.objects.all()
    if request.POST:
        if 'subscribe' in request.POST:
            category = categories.filter(name=request.POST['subscribe']).first()
            category.subscribers.add(request.user)
            messages.success(request, f"Subscribing to {category.name} was successful")
        elif 'unsubscribe' in request.POST:
            category = categories.filter(name=request.POST['unsubscribe']).first()
            category.subscribers.remove(request.user)
            messages.success(request, f"Unsubscribe from {category.name} was successful")
        else:
            pass
        if "next" in request.GET:
            return redirect(request.GET['next'])
    return render(request, "categories/categories.html", {
        'categories': categories,
    })


@login_required()
def get_category(request, category_slug):
    category = get_object_or_404(Categories, slug=category_slug)
    products = category.product.filter(relevant__gte=timezone.now()).all()
    if not products:
        messages.warning(request, f'Category "{category}" is empty')
    return render(request, "categories/category.html", {
        'category': category,
        'products': products
    })


@login_required()
def get_cabinet(request):
    categories = EmailSubscribe.objects.filter(user=request.user).all()
    if request.method == "POST":
        if "send_emails" in request.POST:
            category = categories.filter(category__name=request.POST['send_emails']).first()
            category.send_email = True
            category.save()
        elif "dont_send_emails" in request.POST:
            category = categories.filter(category__name=request.POST['dont_send_emails']).first()
            category.send_email = False
            category.save()
        else:
            pass

    return render(request, "categories/cabinet.html", {
        "categories": categories
    })

@login_required()
def get_search_results(request):
    categories = ""
    products = ""
    if request.method == "POST":
        form = SearchForm(request.POST)
        if not form.is_valid():
            messages.warning(request, 'Form is invalid')
            redirect(reverse("categories:index"))
        q_obj_category = Q()
        q_obj_product = Q()
        search_by = form.cleaned_data['search'].split()
        for word in search_by:
            q_obj_category |= Q(name__icontains=word)
            q_obj_product |= Q(title__icontains=word)
        categories = Categories.objects.filter(q_obj_category).all()
        products = Product.objects.filter(q_obj_product).all()

    return render(request, "categories/search_result.html", {
        'categories': categories,
        'products': products
    })
