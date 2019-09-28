"""teias URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from admin_page.views import index
from admin_page.views import login
from admin_page.views import main
from admin_page.views import personel
from admin_page.views import show
from admin_page.views import mail
from admin_page.views import sended
from admin_page.views import char
from admin_page.views import demir
from admin_page.views import demir
from admin_page.views import dosya
from admin_page.views import result
from admin_page.views import show_2
from admin_page.views import show_3
from admin_page.views import malzeme

urlpatterns = [
    path('admin/',admin.site.urls),


    path('', index),

    path('login/',login),

    path("main/",main),


    path("personel/", personel),


    path("main/personel/", personel),


    path("show/", show),
    path("show_2/",show_2),
    path("show_3/", show_3),
    path("malzeme/",malzeme),
    path("mail/", mail),
    path("mail/sended/", sended),
    path("main/char/", char),
    path("main/demir/", demir),
    path("main/dosya/", dosya),
    path("main/dosya/result/", result),


]
