from django.urls import path
from .views import postListView,postDetailView
from .views import home , display


urlpatterns = [
   # path('', home, name = 'home'),
   path('', postListView.as_view(), name = 'home'),
   path('post/<int:pk>/', postDetailView.as_view(), name = 'post-detail'),

   path('base/common.html/',display , name = 'display')


]  