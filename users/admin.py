from django.contrib import admin

from .models import UserCabinet, SendMails


class SendMailsAdmin(admin.TabularInline):
    model = SendMails


class UserCabinetAdmin(admin.ModelAdmin):
    inlines = (SendMailsAdmin,)
    exclude = ('user',)


admin.site.register(UserCabinet, UserCabinetAdmin)
