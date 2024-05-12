from django.shortcuts import render
from account.models import post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import(
    ListView,
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    )
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


class postCreateView(LoginRequiredMixin, CreateView):
    model = post
    fields = ['title','content','image']
    template_name = 'post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class postUpdateView(LoginRequiredMixin, UpdateView):
    model = post
    fields = ['title','content','image']
    template_name = 'post_create.html'
    # template_name = 'post_detail.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class postDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = post
    success_url = '/'
    template_name = 'post_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def display(request):
    return render(request)