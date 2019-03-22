from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^/$',views.index,name="second"),
    url(r'^help/$',views.help,name="help"),
    
]