"""micro_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from demo import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^signup', views.signup),
    url(r'^signin', views.signin),
    url(r'^signout', views.signout),
    url(r'^post', views.post),
    url(r'^comment', views.comment),
    url(r'^reply', views.reply),
    url(r'^at', views.at),
    url(r'^like', views.like),
    url(r'^letter', views.letter),

]
