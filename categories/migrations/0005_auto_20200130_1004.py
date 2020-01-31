# Generated by Django 3.0.2 on 2020-01-30 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0004_auto_20200123_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailsubscribe',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='subs', to='categories.Categories'),
        ),
        migrations.AlterField(
            model_name='emailsubscribe',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]