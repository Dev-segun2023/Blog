from django.urls import path
from .views import postListView,postDetailView,postCreateView,postUpdateView,postDeleteView
from .views import home , display


urlpatterns = [
   # path('', home, name = 'home'),
   path('', postListView.as_view(), name = 'home'),
   path('post/<int:pk>/', postDetailView.as_view(), name = 'post-detail'),
   path('post/new/', postCreateView.as_view(), name = 'post-create'),
   path('post/<int:pk>/update/', postUpdateView.as_view(), name = 'post-update'),
   path('post/<int:pk>/delete/', postDeleteView.as_view(), name = 'post-delete'),

   path('base/common.html/',display , name = 'display')


]  