"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views #django provides
#login form and stuff for us.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name = 'register'),
    path('', include('blog.urls')),
    #now when I open up localhost:8000,
    #django will come here and see whether the path
    #matches any of these, if it doesn't it just returns 404.
    #what will be sent to the include function will be the unprocessed part
    #already processed localhost:8000/blog, so blog.urls will be sent an empty 
    #string.

    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    #if we don't specify template_name for logout, it'll show a default logout view
    #and a link to redirect users to admin login. not correct.

    path('profile/', user_views.profile, name = 'profile'),
    
]
