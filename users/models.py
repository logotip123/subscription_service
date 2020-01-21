from django.contrib.auth.models import User
from django.db import models

from main_app.models import Categories


class UserCabinet(models.Model):
    user = models.OneToOneField(User, related_name='user_cabinet', on_delete=models.CASCADE, null=True)
    subscriptions = models.ManyToManyField(Categories, through='SendMails')

    def __str__(self):
        return self.user.username


class SendMails(models.Model):
    user_cabinet = models.ForeignKey(UserCabinet, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    send_email = models.BooleanField(default=True)

    def __str__(self):
        return self.category.name
