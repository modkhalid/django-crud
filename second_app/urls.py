from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^a/$',views.index,name="second")
]