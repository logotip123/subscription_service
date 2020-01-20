from django.contrib import admin

from .models import UserCabinet


@admin.register(UserCabinet)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('user',)
