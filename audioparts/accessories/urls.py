from django.urls import path
from . import views

urlpatterns = [
    path('accessories/', views.accessories, name='accessories'),
]