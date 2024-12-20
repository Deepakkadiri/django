"""vtop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls import include
from homepage.views import homePage,dash,dash2,logoutUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage),
    path('ds/',dash),
    path('ds2/',dash2),
    path('ac/',include('academics.urls')),
    path('my/',include('MyInfo.urls')),
    path('In/',include('InfoCorner.urls')),
    path('re/',include('Research.urls')),
    path('ex/',include('Examination.urls')),
    path('se/',include('Services.urls')),
    path('li/',include('Library.urls')),
    path('bo/',include('Bonafide.urls')),
    path('ho/',include('Hostels.urls')),
    path('ot/',include('Others.urls')),
    path('co/',include('Contact.urls')),
    path('gi/',include('Gic.urls')),
    path('pa/',include('Payments.urls')),
    path('cr/',include('Credentials.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path('out',logoutUser),
]
