from django.shortcuts import render
from .models import Semiconductor

def semiconductor (request):
    semiconduct = Semiconductor.objects.all()
    return render (request, 'semiconductor/semiconductor.html', {'semiconduct':semiconduct})

