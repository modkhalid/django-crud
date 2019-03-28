from django.shortcuts import render
from django.views.generic import (View,TemplateView,ListView,DetailView,
                                    UpdateView,CreateView,DeleteView,)
                                    
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse
from . import models
class MyView(View):
    def get(self,request):
        return HttpResponse("this is first view")


class MyTemplate(TemplateView):
    template_name="CBV/index.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['inject_me']="this is demo data for tempate view \n don't take it granted"
        return context

class MyList(ListView):
    model=models.School


class MyDetail(DetailView):
    context_object_name="school_detail"
    model=models.School

    template_name="CBV/school_detail.html"


class MyCreate(CreateView):
    model=models.School
    fields=('name','principal','address')

class MyUpdate(UpdateView):
    fields=('name','principal')
    model=models.School



class MyDelete(DeleteView):
    model=models.School
    success_url=reverse_lazy("cbv:school_list")
