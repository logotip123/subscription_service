from django.urls import path
from .views import user_registration, user_login, user_logout, get_cabinet


app_name = "users"

urlpatterns = [
    path('registration', user_registration, name='registration'),
    path('login', user_login, name='login'),
    path('logout', user_logout, name='logout'),
    path('cabinet', get_cabinet, name='cabinet'),
]