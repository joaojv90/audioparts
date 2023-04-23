from django.urls import path
from . import views

urlpatterns = [
    path('semiconductor/', views.semiconductor, name='semiconductor'),
    path('semiconductorPDF/', views.ToPdf.as_view(), name='semiconductorPDF'),
]