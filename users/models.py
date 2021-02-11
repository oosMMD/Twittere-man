from django.db import models
from django.contrib.auth.models import User


class Followers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    another_user = models.ManyToManyField(User, related_name='another_user')

    def __str__(self):
        return self.user.name


class User(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
