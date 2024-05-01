from django.urls import path
from .views import ContentListView
from .views import home , display


urlpatterns = [
   path('', ContentListView.as_view(), name = 'home'),
   path('base/common.html/',display , name = 'display')


]  