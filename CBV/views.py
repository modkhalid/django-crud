from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

class MyView(View):
    def get(self,request):
        return HttpResponse("this is first view")