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
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        
                    sRoot = settings.STATIC_ROOT      
                    mUrl = settings.MEDIA_URL         
                    mRoot = settings.MEDIA_ROOT       

                    if uri.startswith(mUrl):
                        path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                        path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                        return uri
                    
            if not os.path.isfile(path):
                    raise Exception(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path

    def get(self, request, *args, **kwargs):
        #try:
            template = get_template('accessories/accessoriesPDF.html')
            context = {
                'logo' : '{}{}'.format(settings.STATIC_URL, 'core/img/logo.webp'),
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