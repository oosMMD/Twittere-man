from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.CharField(max_length=150)
    # name = models.OneToOneField(User, on_delete=models.CASCADE, related_name='name')
    # bio = models.CharField(max_length=250, default=None)
    user_slug = models.SlugField(default=None)

    def __str__(self):
        return str(self.name)
