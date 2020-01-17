from django.urls import path

from .views import get_categories, get_index


app_name = "main_app"

urlpatterns = [
    path('', get_index, name='index'),
    path('categories/', get_categories, name='categories'),
]