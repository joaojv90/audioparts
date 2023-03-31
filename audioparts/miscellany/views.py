from django.shortcuts import render
from .models import Miscellany

def miscellany (request):
    miscell = Miscellany.objects.all()
    return render(request, "miscellany/miscellany.html", {'miscell':miscell})
