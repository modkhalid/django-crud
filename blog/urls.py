from django.conf.urls import url
from . import views

app_name="blog"


urlpatterns=[
    url(r'^about/$',views.About.as_view(),name="about"),
    url(r'^$',views.PostList.as_view(),name="post_list"),
    url(r'^post/list/$',views.PostDraftList.as_view(),name="post_list"),
    url(r'^post/list/(?P<pk>\d+)$',views.PostDetail.as_view(),name="post_detail"),
    url(r'^post/create/$',views.PostCreate.as_view(),name="post_create"),
    url(r'^post/update/(?P<pk>\d+)$',views.PostUpdate.as_view(),name="post_update"),
    url(r'^post/delete/(?P<pk>\d+)$',views.PostDelete.as_view(),name="post_delete"),
    url(r'^post/detail/publish/(?P<pk>\d+)$',views.publish_post,name="post_publish"),
]