""" 
Note : This is the urls.py for this particular
app. When this app is opened it maps the urls 
to respective views. Different from the project
level urls.py main one we saw earlier which is referred 
by django at first.

"""

from django.urls import path
from . import views
from .views import (
    PostListView,
     PostDetailView, 
     PostCreateView,
     PostUpdateView,
     PostDeleteView,
     UserPostListView
     )


urlpatterns = [
    path('', PostListView.as_view(), name = "blog-home"),
    #'' is empty, meaning no localhost:8000/anything
    #required, it'll be there by default.

    path('user/<str:username>', UserPostListView.as_view(), name = "user-posts"),
    #things inside angled brackets <> are url variables.

    #django comes here from the main urls.py, and matches the pattern
    #given to it by the include function.
    path('about/', views.about, name = "blog-about"),

    #NOTE: you do not need to put path for about into the main urls.py
    #why? this is a subdirectory (say) for THIS app.
    #you can access it using localhost:8000/blog/about.
    #/blog sends django here, /about activates the about page.


    path('post/<int:pk>/', PostDetailView.as_view(), name = "post-detail"),
    #we have to create a url pattern with a variable, why? because we are looking
    #into details of a particular post.
    #since this refers to a particular post, pk here is the primary key of the post


    path('post/new/', PostCreateView.as_view(), name = "post-create"),

    path('post/<int:pk>/update', PostUpdateView.as_view(), name = "post-update"),
    # we just need to pass in the primary key of what we need to update, the 
    #django view will take care of the rest.

    path('post/<int:pk>/delete', PostDeleteView.as_view(), name = "post-delete"),
    #post delete url



] 