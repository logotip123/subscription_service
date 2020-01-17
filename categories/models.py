from django.db import models
from subscription_service.settings import PROJECT_VARIABLES

class Categories(models.Model):
    name = models.CharField(max_length=PROJECT_VARIABLES["category_name_max_length"])
    created = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

