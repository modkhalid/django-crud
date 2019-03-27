from django.shortcuts import render
from django.views.generic import View,TemplateView
from django.http import HttpResponse

class MyView(View):
    def get(self,request):
        return HttpResponse("this is first view")


class MyTemplate(TemplateView):
    template_name="CBV/index.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['inject_me']="this is demo data for tempate view \n don't take it granted"
        return context
