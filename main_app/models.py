import datetime

from django.db import models
from django.utils.text import slugify

from subscription_service.settings import PROJECT_VARIABLES


class Categories(models.Model):
    name = models.CharField(unique=True, max_length=PROJECT_VARIABLES["category_name_max_length"])
    slug = models.SlugField(unique=True, null=True)
    created = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=PROJECT_VARIABLES["product_title_max_length"])
    slug = models.SlugField(unique=True)
    created = models.DateField(auto_now_add=True)
    relevant = models.DateTimeField(verbose_name="Relevant until")
    description = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:
            date = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
            self.slug = slugify(str(self.title) + date)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title