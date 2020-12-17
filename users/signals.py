#some functions should automatically execute on some action.
#in this case, profile needs to be created every time a user is registered.

from django.db.models.signals import post_save #signal that gets fired when an object is saved.
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender,instance, created, **kwargs):
    #this executes everytime a user is created.
    if(created):
        Profile.objects.create(user=instance)


#@receiver(post_save, sender = User)
#def create_profile(sender,instance, **kwargs):
#    instance.profile.save()






