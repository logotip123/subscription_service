from django.urls import path

from .views import get_categories, get_index, get_category, get_cabinet, get_search_results


app_name = "categories"

urlpatterns = [
    path('', get_index, name='index'),
    path('categories/', get_categories, name='categories'),
    path('categories/<category_slug>', get_category, name='category'),
    path('cabinet/', get_cabinet, name='cabinet'),
    path('search_result/', get_search_results, name='search_result'),
]