from django.shortcuts import render
from .models import Accessory

def accessories (request):
    accessory = Accessory.objects.all()
    return render(request, "accessories/accessories.html", {'accessory':accessory})
