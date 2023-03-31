from django.shortcuts import render
from .models import Audio

def audio (request):
    sound = Audio.objects.all()
    return render(request, "audio/audio.html", {'sound':sound})