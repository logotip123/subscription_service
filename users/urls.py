from django.urls import path
from .views import user_registration, user_login


app_name = "users"

urlpatterns = [
    path('registration', user_registration, name='registration'),
    path('login', user_login, name='login'),
]