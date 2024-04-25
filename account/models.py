from django.db import models
<<<<<<< HEAD
from base.models import User



class profile(models.Model):
=======
# from django.contrib.auth.models import User
from base.models import User


class Profile(models.Model):
>>>>>>> parent of 4bbdbee (deleted html not in template)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')

    def __str__(self):
        return f'{self.user.email} profile'

<<<<<<< HEAD
=======

>>>>>>> parent of 4bbdbee (deleted html not in template)

# Create your models here.
