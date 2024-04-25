from django.db.models.signals import post_save
from base.models import User
from django.dispatch import receiver
<<<<<<< HEAD
from .models import profile


@receiver(post_save, sender=User)
def create_Profile(sender,instance,created,**kwargs):
    if created:
        profile.objects.create(user=instance)
=======
from .models import Profile


@receiver(post_save, sender = User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
>>>>>>> parent of 4bbdbee (deleted html not in template)




<<<<<<< HEAD
@receiver(post_save, sender=User)
def save_Profile(sender,instance,**kwargs):
    instance.profile.save()
=======
@receiver(post_save, sender = User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
>>>>>>> parent of 4bbdbee (deleted html not in template)
