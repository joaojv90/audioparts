from .models import Social

def ctx_dict(request):
    ctx = {}
    socialList = Social.objects.all()
    for social in socialList:
        ctx[social.key]=social.link
    return ctx