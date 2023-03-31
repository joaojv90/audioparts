from django.urls import path
from . import views

urlpatterns = [
    path('miscellany/', views.miscellany, name='miscellany'),
]