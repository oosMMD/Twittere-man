from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=60)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    auth_slug = models.SlugField(default=None)
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug

    def editedbody(self):
        if len(self.body) > 120:
            return self.body[:120] + '  ...'
        else:
            return self.body


class Answer(models.Model):
    answer = models.TextField()
    target = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='target')
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')

    def __str__(self):
        return self.answer[:10]

