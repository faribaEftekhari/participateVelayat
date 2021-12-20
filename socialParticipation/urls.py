"""socialParticipation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index,name='index'),
    path('',views.home,name=''),    
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('afterlogin',views.afterlogin_view,name='afterlogin'),
    path('logout',views.logout_view,name='logout'),
    path('registerSaman',views.registerSaman_view,name='registerSaman'),
    path('addbaner',views.addbaner_view,name='addbaner'),
    path('addnews',views.addnews_views,name='addnews'),
    path('addparticipate',views.addparticipate_view,name='addparticipate'),
    path('registerVolenteer',views.addvolenteer_view,name='registerVolenteer'),
    path('volenteers',views.showvolenteer_view,name='volenteers'),
    path('delvolenteer/<int:pk>',views.deletevolenteer_view,name='delvolenteer'),
    path('newsdetail/<int:pk>',views.newsdetail_view,name='newsdetail'),
    path('delsaman/<int:pk>',views.deletesaman_view,name='delsaman'),
    path('editprofile',views.editprofile_view,name='editprofile'),
    path('search',views.search_view,name="search"),   
    path('archive/<str:pk>/',views.archive_views,name='archive'),
    path('specialnews/<int:pk>',views.specialnews_view,name="specialnews"),
    path('messageadmin',views.messageadmin_view,name='messageadmin'),
    path('showmessage',views.showmessage_view,name='showmessage'),
    path('delnews/<int:pk>',views.delnews_view,name='delnews'),
    path('delbaner/<int:pk>',views.delbaner_view,name='delbaner'),
    path('delparticipate/<int:pk>',views.delparticipate_view,name='delparticipate'),
    path('partnews/<int:pk>',views.partnews_view,name='partnews'),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
