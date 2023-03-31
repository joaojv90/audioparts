from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def contacts(request):
    return render(request, 'core/contacts.html')

def privacypolicy(request):
    return render(request, 'core/privacypolicy.html')

def about(request):
    return render(request, 'core/about.html')

def error404(request, exception):
    return render(request, 'core/error404.html')
