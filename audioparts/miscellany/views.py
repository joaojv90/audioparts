import os
from weasyprint import HTML, CSS
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from django.conf import settings
from .models import Miscellany

def miscellany (request):
    miscell = Miscellany.objects.all()
    return render(request, "miscellany/miscellany.html", {'miscell':miscell})

class ToPdf(View):
    def get(self, request, *args, **kwargs):
        try:
            template = get_template('miscellany/miscellanyPDF.html')
            context = {
                'miscell': Miscellany.objects.all(),
            }
            html = template.render(context)
            css_url = os.path.join(settings.BASE_DIR, 'staticfiles/core/css/style.css')
            pdf = HTML(string=html, base_url=request.build_absolute_uri()).write_pdf(stylesheets=[CSS(css_url)])
            return HttpResponse(pdf, content_type='application/pdf')
        except:
            pass
        return render(request, "core/index.html")
