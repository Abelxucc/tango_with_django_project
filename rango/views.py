from django.shortcuts import render
from django.http import  HttpResponse
# Create your views here.

from django.shortcuts import render
from django.conf import settings

def index(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'author_name': 'Jiacheng Xu'}
    return render(request, 'rango/about.html', context=context_dict)

def show_media(request):
    return render(request, 'rango/show_media.html', {'media_url': settings.MEDIA_URL})

def new_view(request):
    context_dict = {'title': 'Welcome!', 'content': 'This is a new page using a template.'}
    return render(request, 'rango/new_template.html', context=context_dict)