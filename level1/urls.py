"""level1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import url,include
# from django.contrib import admin
from first_app import views 
# from django.contrib.auth import views as v
# from second_app import views as v2
# from CBV import views as cbviews
from django.conf.urls import url,include
from django.contrib import admin
# from bloging import view
# from django.contrib.auth import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('blog.urls')),
    url(r'^second/',include('second_app.urls')),
    url(r'^login/$',views.user_login,name='user_login'),
    url(r'^logout/$',views.user_logout,name='user_logout'),
    # url(r'accounts/login/$',views.login,name='login'),
    # url(r'accounts/logout/$',views.logout,kwargs={'next_page':'/'},name='logout'),
    url(r'^cbv/', include('CBV.urls')),
    url(r'^blog/', include('blog.urls')),
]
