from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import Backlight
from .utils import render_to_pdf

def backlight (request):
    strips = Backlight.objects.all()
    return render (request, "backlight/backlight.html",
                   {'strips':strips})

class Listapdf(View):
    def get (self, request, *args, **kwargs):
        strips = Backlight.objects.all()
        #link_callback()
        data = {'strips':strips}
        pdf = render_to_pdf('backlight/viewpdf.html', data)
        return HttpResponse(pdf, content_type = 'application/pdf')