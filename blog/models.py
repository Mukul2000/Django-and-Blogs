from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=1600)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # we are not using timezone.now() because we dont want
    # to call the function, we are just passing a reference
    # of the function
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    # cascade deletes all comments if a post is deleted.
    # sort of foreign key that connects a comment to a post

    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return f'{self.post.title}-{self.name}'
