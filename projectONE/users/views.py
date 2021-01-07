from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    #The conditional statement below verifies that the data 
    # that is added by the user is actually valid.
    #------------------------------------------------------
    #This is done by using a method known as message from 'django.contrib'
    #This method comes in various types;
    #-----------------------------1.message.debug
    #-----------------------------2.message.info
    #-----------------------------3.message.success
    #-----------------------------4.message.warning
    #-----------------------------5.message.error
    #In this case we are checking if 
    # the data is valid so message.success will be used here
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account successfully created for {username}, you can now LogIn!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    #Posts the users info and puts them into the fields.
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES,
                                   instance=request.user.profile)
        #Checks if the users data is valid, if it is is. IT SAVES
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Account info was successfully updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        #Sending both forms as contexts to the profile.html. Not forgetting to 
        #return it at the end
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)