from django.urls import path
from .views import get_index


app_name = "mainapp"

urlpatterns = [
    path('', get_index, name='index'),
]