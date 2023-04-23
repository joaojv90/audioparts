import os
from weasyprint import HTML, CSS
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from django.conf import settings
from .models import Audio

def audio (request):
    sound = Audio.objects.all()
    return render(request, "audio/audio.html", {'sound':sound})

class ToPdf(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('audio/audioPDF.html')
            context = {
                'sound': Audio.objects.all(),
            }
            html = template.render(context)
            css_url = os.path.join(settings.BASE_DIR, 'staticfiles/core/css/style.css')
            pdf = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(stylesheets=[CSS(css_url)])
            return HttpResponse(pdf, content_type='application/pdf')
        except:
            pass
        return render(request, "core/index.html")