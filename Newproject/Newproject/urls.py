"""Newproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('logo/', views.logo),
     path('', views.home_page),
    path('location/', views.location_page),
    path('signup/', views.signup_page),
    path('logout/', views.logout_page),
    path('dinging/', views.dining_page),
    path('gallary/', views.gallary_page),
    path('gallary-dining/', views.Gallary_dinging_page),
    path('gallary-facility/', views.Gallary_facility_page),
    path('facility/', views.facility),
    path('time/', views.timming_ticket),
    path('contact/', views.Contact_us),
    path('Book/', views.Book_page),
    #footer page all URL
    path('aboutus/', views.aboutus_page),
    path('privacy/', views.Privacy_Policy),
    path('term/', views.term_conditions),
    path('refund/', views.refund),
      path('', views.support),
    path('accounts/', include("django.contrib.auth.urls")),
]
