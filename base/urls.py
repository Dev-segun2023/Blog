from django.urls import path
from .views import postListView,postDetailView,postCreateView,postUpdateView
from .views import home , display


urlpatterns = [
   # path('', home, name = 'home'),
   path('', postListView.as_view(), name = 'home'),
   path('post/<int:pk>/', postDetailView.as_view(), name = 'post-detail'),
   path('post/new/', postCreateView.as_view(), name = 'post-create'),
   path('post/<int:pk>/update/', postUpdateView.as_view(), name = 'post-update'),

   path('base/common.html/',display , name = 'display')


]  