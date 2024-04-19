from django.urls import path
from .views import home , display


urlpatterns = [
   path('', home, name = 'home'),
   path('base/common.html/',display , name = 'display')


]