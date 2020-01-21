# Generated by Django 3.0.2 on 2020-01-20 14:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_remove_usercabinet_a'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercabinet',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_cabinet', to=settings.AUTH_USER_MODEL),
        ),
    ]
