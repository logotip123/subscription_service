from django.urls import path, include
from rest_framework import routers

from . import views


app_name = "categories"

router = routers.DefaultRouter()
router.register('categories', views.CategoriesViewSet)
router.register('products', views.ProductsViewSet)

urlpatterns = [
    path('', views.get_index, name='index'),
    path('categories/', views.get_categories, name='categories'),
    path('categories/<category_slug>', views.get_category, name='category'),
    path('cabinet/', views.get_cabinet, name='cabinet'),
    path('search_result/', views.get_search_results, name='search_result'),
    path('api/', include(router.urls)),
]