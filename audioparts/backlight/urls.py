from django.urls import path
from . import views

urlpatterns = [
    path('backlight/', views.backlight, name='backlight'),
]