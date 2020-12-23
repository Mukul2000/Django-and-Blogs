from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html',context)
    #render by default looks in template directory for the app.

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #template of the form <app>/<model>_<viewtype>.html
    context_object_name = 'posts' #inside home.html, posts is the variable we used to access posts
    ordering = ['-date_posted'] #'date-posted' gives normal sorting, adding '-' sorts in reverse.

"""
So, what's the difference between class based views and functional views?
it's just setting some variables.

Function based views require a base template, then some context and stuff.

Much easier to use class based views.

"""

class PostDetailView(DetailView):
    model = Post
    #this class will be looking for template <app>/<model>_<viewtype>.html
    # i.e blog/post_detail.html

    

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})
