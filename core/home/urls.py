from django.contrib import admin
from django.urls import path,include
from .views import home,about

urlpatterns = [
    path('', home, name='home'),  # Home view
    path('about/', about, name='about'),  # About view
    ]
