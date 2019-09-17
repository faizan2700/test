"""websolutions URL Configuration

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
from django.urls import path, include
from django.views.generic import RedirectView
from . import views
urlpatterns = [
    path('',RedirectView.as_view(url = '/home/', permanent=True)),
    path('home/',views.home, name = 'home'),
    path('about/',views.about_us, name = 'about-us'),
    #path('vision-and-mission/',views.vision,name='vision-and-mission'),
    #path('FAQ/',views.faq,name='FAQ'),
    path('marketing-partners/',views.marketing_partners,name='marketing-partners'),
    path('partner-registeration/',views.par_registeration.as_view(),name='par-reg'),
    path('work/',views.work,name='work'),
    path('contact-us/',views.Contact.as_view(),name = 'contact-us'),
    path('services/',views.services,name='services'),
    path('pricing/',views.pricing,name='pricing'),
]
