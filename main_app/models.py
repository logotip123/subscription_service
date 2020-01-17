from django.db import models
from subscription_service.settings import PROJECT_VARIABLES


class Categories(models.Model):
    name = models.CharField(unique=True, max_length=PROJECT_VARIABLES["category_name_max_length"])
    slug = models.SlugField(unique=True)
    created = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=PROJECT_VARIABLES["product_title_max_length"])
    slug = models.SlugField(unique=True)
    created = models.DateField(auto_now_add=True)
    relevant = models.DateTimeField(verbose_name="Relevant until")
    description = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title