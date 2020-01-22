from django.contrib import admin

from .models import Categories, Product, SendMails


class SendMailsAdmin(admin.TabularInline):
    model = SendMails


class CategoriesAdmin(admin.ModelAdmin):
    fields = ('name', 'description')
    inlines = (SendMailsAdmin,)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('title', 'relevant', 'category')

admin.site.register(Categories, CategoriesAdmin)