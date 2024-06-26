from django.db import models
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.


#create your CustomUserManager here
class CustomUserManager(BaseUserManager):
    def create_user(self, email,  password,   **extra_fields):
        if not email:
            raise ValueError('Email must be provided')
        if not password:
            raise ValueError('Password must be provided')
        
        user = self.model(
            email = self.normalize_email(email),
            # first_name = first_name,
            # last_name = last_name,            
            password = password,
            
            **extra_fields
        )

        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True),
        extra_fields.setdefault('is_active', True),
        extra_fields.setdefault('is_superuser', True),
        return self.create_user(email, password, **extra_fields)
        



    # def create_user(self, email, first_name, last_name, password, **extra_fields):
    #     first_name = first_name,
    #     last_name = last_name,
    #     extra_fields.setdefault('is_staff', False),
    #     extra_fields.setdefault('is_active', False),
    #     extra_fields.setdefault('is_superuser', False),
    #     return self._create_user(email, first_name , last_name, password)
    



# class UserManager(BaseUserManager):
#     def _create_user(self, email, first_name, last_name, password,   **extra_fields):
#         if not email:
#             raise ValueError('Email must be provided')
#         if not password:
#             raise ValueError('Password must be provided')
        
#         user = self.model(
#             email = self.normalize_email(email),
#             first_name = first_name,
#             last_name = last_name,            
#             password = password,
            
#             **extra_fields
#         )

#         user.set_password(password)
#         user.save()
#         return user
#create your User Model here
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length=240, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=250)
    # mobile = models.CharField(max_length=50)


    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)


    objects = CustomUserManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []















    

    
# Create your models here.