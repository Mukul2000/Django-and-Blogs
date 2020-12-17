from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

def register(request):
    #this is used everytime render is called.
    #so when the user will submit, user will be redirected back here.
    #checking if the request is POST will tell to take some other course
    #of action.
    if(request.method == 'POST'):
        form = UserRegisterForm(request.POST)
        if(form.is_valid()):
            form.save() #registers the user.
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login') #redirect to 
            #login page after you register
    form = UserRegisterForm()
    return render(request,'users/register.html', {'form': form})

#neccessary to prevent a user from going to /profile directly from 
#address bar
@login_required 
def profile(request):
    return render(request, 'users/profile.html')
