from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Post
from django.views.generic import DetailView


# Create your views here.
def home_view(request):
  return render(request,'home/index.html')
  
def about_view(request):
  return render(request,'home/about.html')
  
def contact_view(request):
  return render(request,'home/contact.html')
  
class PostListView(ListView):
    model = Post
    template_name = 'home/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'home/post_detail.html'
    context_object_name = 'post'