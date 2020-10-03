"""resdown URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from myapp.api import ResList,Base,Add_Res,DownRes


urlpatterns = [
    path('',Base.as_view(),name='Base'),
    path('admin/', admin.site.urls),
    url(r'^api/res_list/$',ResList.as_view(),name='res_list'),
    url(r'^api/add_res/$',Add_Res.as_view(),name = 'add_res'),
    url(r'^api/res_list/(?P<res_id>[0-9]+)/$',DownRes.as_view(),name='down_res'),
    #url(r'^api/player_details/(?P<player_id>\d+)/$',PlayerDetails.as_view(),name='player_details'),
    #url(r'^api/teams_list/$',TeamsList.as_view(),name='teams_list')
]
