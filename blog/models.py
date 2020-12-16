from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
     title = models.CharField(max_length = 1600)
     content = models.TextField()
     date_posted = models.DateTimeField(default=timezone.now)
     #we are not using timezone.now() because we dont want 
     #to call the function, we are just passing a reference
     #of the function
     author = models.ForeignKey(User, on_delete = models.CASCADE)

     def __str__(self):
          return self.title