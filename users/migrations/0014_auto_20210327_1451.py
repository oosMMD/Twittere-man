# Generated by Django 3.1.6 on 2021-03-27 10:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0013_auto_20210327_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='other_guy',
            field=models.ManyToManyField(default='sinarayo', related_name='other_guy', to=settings.AUTH_USER_MODEL),
        ),
    ]