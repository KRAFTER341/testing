from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.abaut, name='about'),
    path('contacts', views.contacts, name='contacts'),
]