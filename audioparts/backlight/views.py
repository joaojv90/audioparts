from django.shortcuts import render
from .models import Backlight

def backlight (request):
    strips = Backlight.objects.all()
    return render (request, "backlight/backlight.html",
                   {'strips':strips})