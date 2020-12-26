from django.shortcuts import render
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# UserPassesTestMixin is to prevent non authors of a post from editing the post

class PostListView(ListView):
    model = Post
    # template of the form <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html'
    # inside home.html, posts is the variable we used to access posts
    context_object_name = 'posts'
    # 'date-posted' gives normal sorting, adding '-' sorts in reverse.
    ordering = ['-date_posted']


"""
So, what's the difference between class based views and functional views?
it's just setting some variables.

Function based views require a base template, then some context and stuff.

Much easier to use class based views.

"""


class PostDetailView(DetailView):
    model = Post
    # this class will be looking for template <app>/<model>_<viewtype>.html
    # i.e blog/post_detail.html


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    # unlike other views, it shares template with update
    # looks form <model>_form.html
    success_url = ''

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    # unlike other views, it shares template with update
    # looks form <model>_form.html
    success_url = ''

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):  # used with userpassestestmixin to prevent non authors
        # from messing with other people's posts.
        post = self.get_object()
        if(self.request.user == post.author):
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url='/'
    def test_func(self):  # used with userpassestestmixin to prevent non authors
        # from deleting people's posts.
        post = self.get_object()
        if(self.request.user == post.author):
            return True
        else:
            return False
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
