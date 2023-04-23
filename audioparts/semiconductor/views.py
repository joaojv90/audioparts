import os
from weasyprint import HTML, CSS
from django.shortcuts import render
from .models import Semiconductor
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from django.conf import settings

def semiconductor (request):
    semiconduct = Semiconductor.objects.all()
    return render (request, 'semiconductor/semiconductor.html', {'semiconduct':semiconduct})

class ToPdf(View):
    def get(self, request, *args, **kwargs):
        #try:
            template = get_template('semiconductor/semiconductorPDF.html')
            context = {
                'logo' : '{}{}'.format(settings.STATIC_URL, 'logotipo.webp'),
                'semiconduct': Semiconductor.objects.all(),
            }
            html = template.render(context)
            css_url = os.path.join(settings.BASE_DIR, 'staticfiles/core/css/style.css')
            #css_url = os.path.join(settings.BASE_DIR, 'staticfiles/core/css/bootstrap.min.css')
            pdf = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(stylesheets=[CSS(css_url)])
            return HttpResponse(pdf, content_type='application/pdf')
        #except:
            #pass
        #return render(request, "core/index.html")