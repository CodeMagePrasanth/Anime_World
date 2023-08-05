"""
URL configuration for Naruto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('Anime_World/',Anime_World,name='Anime_World'),
    path('geek/',geek,name='geek'),
    path('webpage3/',webpage3,name='webpage3'),
    path('hubspot/',hubspot,name='hubspot'),
    path('blacksheep/',blacksheep,name='blacksheep'),
    path('reg_form/',reg_form,name='reg_form'),
    path('IconGallery/',IconGallery,name='IconGallery'),
    path('Wakeup_To_Relality/',Wakeup_To_Relality,name='Wakeup_To_Relality'),
    path('IT_Company/',IT_Company,name='IT_Company'),
    path('MDB/',MDB,name='MDB'),
    path('form_page/',form_page,name='form_page'),
    path('bootstrap/',bootstrap,name='bootstrap'),
    path('jiraiya/',jiraiya,name='jiraiya'),
    path('signup_page/',signup_page,name='signup_page'),
    path('SignIn/',SignIn,name='SignIn'),
    path('course/',course,name='course'),
]
