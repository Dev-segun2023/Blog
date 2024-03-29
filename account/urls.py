from django.urls import path
from .views import Sign_up



urlpatterns = [
    path('Signup/', Sign_up, name= ' signup'),
]