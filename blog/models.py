from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # to fix an error where the post is created but doesn't know where to go, so the reverse enters a string to the new post
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
