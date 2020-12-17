from django.db import models
from django.contrib.auth.models import User

#one to one relationship of user and profile.
#one user can have only one profile

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    #cascade means if user is deleted, then delete the profile.

    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

