from django.shortcuts import render
from django.http import HttpResponse
from second_app.models import AccessRecord
from .forms import FormName,WebForm
# Create your views here.
def index(request):
#     dic={'content':"hello my name is khalid khan"}
#     return render(request,'index.html',context=dic)
        return render(request,'first_app/other.html')

def help(request):
    dic={'help':'i cant help'}
    return render(request,"help.html",context=dic)

def dater(request):
    date_list=AccessRecord.objects.order_by('date')
    # print(date_list[0].name)
    dic={'my_list':date_list}
    return render(request,'list.html',context=dic)


def form(request):
    name=""
    form=FormName()
    if request.method =='POST':
        form=FormName(request.POST)
        
        if form.is_valid():
            name=form.cleaned_data
    return render(request,'form.html',{'form':form,'name':name})


def upload_page(request):
    form=WebForm()
    if request.method =='POST':
        # print(request.POST)
        form=WebForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
    return render(request,'form.html',{'form':form})
