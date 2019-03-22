from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    dic={'content':"hello my name is khalid khan"}
    return render(request,'index.html',context=dic)

def help(request):
    dic={'help':'i cant help'}
    return render(request,"help.html",context=dic)