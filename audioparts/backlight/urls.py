from django.urls import path
from . import views

urlpatterns = [
    path('backlight/', views.backlight, name='backlight'),
    path('viewpdf/', views.Listapdf.as_view(), name='viewpdf'),
]