from django.urls import path
from . import views

urlpatterns = [
    path('audio/', views.audio, name='audio'),
    path('audioPDF/', views.ToPdf.as_view(), name='audioPDF'),
]