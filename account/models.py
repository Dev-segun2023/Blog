from django.db import models
from base.models import User

 



class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')

    def __str__(self):
        return f'{self.user.email} profile'


# class Userupdate(User):
#     email = User.email

#     class Meta:
#         models = User
#         fields = 'email'
    
 
# Create your models here.
