from django.contrib.auth.models import User
from django.db import models

from main_app.models import Categories


class UserCabinet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    subscriptions = models.ManyToManyField(Categories)

    def __str__(self):
        return self.user.username