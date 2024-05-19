from django.db import models
from django.utils import timezone
from base.models import User
from django.urls import reverse

 



class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pic')

    def __str__(self):
        return f'{self.user.email} profile'
    

class post(models.Model):
    title = models.CharField(max_length=100)
    post_image = models.ImageField(default='default.jpg', upload_to='media')        
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
    
    def snippet(self):
        return self.content[:50] + '...'





    
    

    # def __str__(self):
    #     return self.title

# class Userupdate(User):
#     email = User.email

#     class Meta:
#         models = User
#         fields = 'email'
    
 
# Create your models here.
