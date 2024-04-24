from django.urls import path
from .views import Sign_up, Login,Logout, profile




urlpatterns = [
    path('Signup/', Sign_up, name= 'signup'),
    path('login/', Login, name= 'login'),
    path('logout/',Logout, name= 'logout'),
    path('profile/', profile, name= 'profile')
]