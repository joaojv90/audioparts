from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contactos/', views.contacts, name='contacts'),
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    path('error404/', views.error404, name='error404'),
    path('about/', views.about, name='about'),
]
