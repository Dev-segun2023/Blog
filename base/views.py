from django.shortcuts import render
from .models import Content
from django.views.generic import ListView
# Create your views here.


def home(request):
    show = Content.objects.all()
    return render(request, 'home.html', {'show': show})




class ContentListView(ListView):
    model = Content
    template_name = 'home.html'
    context_object_name = 'show'


def display(request):
    return render(request)