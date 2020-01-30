from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Categories(models.Model):
    name = models.CharField(unique=True, max_length=250)
    slug = models.SlugField(unique=True, null=True)
    created = models.DateField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    subscribers = models.ManyToManyField(User, through="EmailSubscribe")

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class EmailSubscribe(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING, related_name='subs')
    send_email = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.category.name}: {str(self.send_email)}"


class Product(models.Model):
    title = models.CharField(max_length=250)
    created = models.DateField(auto_now_add=True)
    relevant = models.DateTimeField(verbose_name="Relevant until")
    description = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='product')

    def save(self, *args, **kwargs):
        if not self.id:
            pass
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
