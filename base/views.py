from django.shortcuts import render
from account.models import post
from django.views.generic import ListView,DetailView
# Create your views here.


def home(request):
    show = post.objects.all()
    # return render(request, 'home.html',context={'show': show})




class postListView(ListView):
    model = post           #<app>/<model>_<viewtype>.html
    template_name = 'home.html'
    context_object_name = 'show'
    ordering = ['-date_posted'] 


class postDetailView(DetailView):
    model = post
    template_name = 'post_detail.html'
    # context_object_name = 'object'
    # ordering = ['-date_posted'] 


def display(request):
    return render(request)