from django.conf.urls import url
from . import views 

app_name="cbv"

urlpatterns=[
    url(r'^view/$', views.MyView.as_view(),name="view"),
    url(r'^template/$',views.MyTemplate.as_view(),name="template"),
    url(r'^list/$',views.MyList.as_view(),name="school_list"),
    url(r'^detail/(?P<pk>\d+)/$',views.MyDetail.as_view(),name="school_detail"),
    url(r'^create/$',views.MyCreate.as_view(),name="school_create"),
    url(r'^update/(?P<pk>\d+)/$',views.MyUpdate.as_view(),name="update"),
    url(r'^delete/(?P<pk>\d+)/$',views.MyDelete.as_view(),name="Delete"),
]