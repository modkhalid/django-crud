from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    return render(request,'first_app/other.html')

from .forms import UserForm,USerProfileForm

def registration(request):

    registered=False
    if request.method=='POST':
        user_form=UserForm(request.POST)
        profile_form=USerProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
                # print("yes it is ",profile.profile_pic)
            # print(request.FILES)

            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=USerProfileForm()

    return render(request,'first_app/register.html',{'registered':registered,'user_form':user_form,'profile':profile_form})



def user_login(request):
    if request.method=='POST':
        # print(request.POST)
        data=request.POST
        username=data.get('username')
        password=data.get('password')

        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)

                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("<h1>You are not login mother fucker</h1>")
        else:
            print("user name: {} and password {} are wrong".format(username,password))
            return HttpResponseRedirect(reverse('user_login'))
            
    return render(request,'first_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

    