from django.urls import path

from .views import get_categories


app_name = "categories"

urlpatterns = [
    path('', get_categories, name='index'),
]