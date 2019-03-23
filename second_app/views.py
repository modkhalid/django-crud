from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import AccessRecord
# Create your views here.
def index(request):
    dic={'content':"hello my name is khalid khan"}
    return render(request,'index.html',context=dic)

def help(request):
    dic={'help':'i cant help'}
    return render(request,"help.html",context=dic)

def dater(request):
    date_list=AccessRecord.objects.order_by('date')
    # print(date_list[0].name)
    dic={'my_list':date_list}
    return render(request,'list.html',context=dic)
