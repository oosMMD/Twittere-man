from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, related_name='name')
    other_user = models.ManyToManyField(User, related_name='other_user')

    def __str__(self):
        return self.name
