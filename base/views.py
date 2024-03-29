from django.shortcuts import render
from .models import Content
# Create your views here.


def home(request):
    show = Content.objects.all()
    return render(request, 'index.html', {'show': show})