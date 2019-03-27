from django.conf.urls import url
from . import views 

app_name="cbv"

urlpatterns=[
    url(r'^view/$', views.MyView.as_view()),
    url(r'^template/$',views.MyTemplate.as_view())
]