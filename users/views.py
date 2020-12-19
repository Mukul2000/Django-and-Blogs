from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
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
    if(request.method == "POST"): #this will be run when form is submitted.
        #remember that once a form is submitted, the POST request
        #is sent back to the original route from which it came from
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)    

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()  
            messages.success(request, "Your Account has been updated")
            return redirect('profile')      
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)


