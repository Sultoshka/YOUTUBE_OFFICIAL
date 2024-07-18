"""
URL configuration for videoproj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django import views
from django.urls import path
from django.contrib import admin
from django.urls import path
from proj.app.views import video_list, video_detail, add_video, add_comment, register_user, \
    add_favorite_video, remove_favorite_video, favorite_videos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', video_list, name='video_list'),
    path('video/<int:pk>/', video_detail, name='video_detail'),
    path('add_video/', add_video, name='add_video'),
    path('video/<int:pk>/add_comment/', add_comment, name='add_comment'),
    path('register/', register_user, name='register_user'),
    path('add_video/', add_video, name='add_video'),
    path('video/<int:video_id>/add_favorite/', add_favorite_video, name='add_favorite_video'),
    path('video/<int:video_id>/remove_favorite/', remove_favorite_video, name='remove_favorite_video'),
    path('favorites/', favorite_videos, name='favorite_videos'),
]
