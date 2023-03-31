from django.urls import path
from . import views

urlpatterns = [
    path('audio/', views.audio, name='audio'),
]