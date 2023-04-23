import os
from django.conf import settings
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from django.urls import reverse
from .models import Accessory

def accessories (request):
    accessory = Accessory.objects.all()
    return render(request, "accessories/accessories.html", {'accessory':accessory})

class ToPdf (View):
    accessory = Accessory.objects.all()

    def link_callback(self, uri, rel):
        sUrl = settings.STATIC_URL        
        sRoot = settings.STATIC_ROOT      
        mUrl = settings.MEDIA_URL         
        mRoot = settings.MEDIA_ROOT       

        if uri.startswith(mUrl):
            return os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            return os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri
            

    def get(self, request, *args, **kwargs):
        #try:
            template = get_template('accessories/accessoriesPDF.html')
            print(settings.STATIC_ROOT)
            context = {
                'logo' : '{}{}'.format(settings.STATIC_URL, 'logotipo.webp'),
                'accessory': Accessory.objects.all(),
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="Catálogo Accesorios AudioParts.pdf"'
            pisa_status = pisa.CreatePDF(
                html, dest=response, link_callback=self.link_callback)
            return response
        #except:
            #pass
        #return render(request, "core/index.html")