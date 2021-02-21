from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    name = models.CharField(max_length=150)
    # bio = models.CharField(max_length=250)
    user_slug = models.SlugField(default=None)

    def __str__(self):
        return str(self.name)


class Follow(models.Model):
    me = models.OneToOneField(User, on_delete=models.CASCADE, related_name="me")
    other_guy = models.ManyToManyField(User, blank=True, related_name='other_guy')

    def __str__(self):
        return str(self.me)
