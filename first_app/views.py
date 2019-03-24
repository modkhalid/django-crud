from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("hello world")

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

    return render(request,'first_app/register.html',{'registered':registered,'user':user_form,'profile':profile_form})

