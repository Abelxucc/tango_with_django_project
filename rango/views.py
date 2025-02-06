from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from rango.models import Category, Page
from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):
    boldmessage = 'Crunchy, creamy, cookie, candy, cupcake!'
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {
        'boldmessage': boldmessage,
        'categories': category_list,
        'pages': page_list
    }

    return render(request, 'rango/index.html', context=context_dict)



def about(request):
    context_dict = {'author_name': 'Jiacheng Xu'}
    return render(request, 'rango/about.html', context=context_dict)

def show_media(request):
    return render(request, 'rango/show_media.html', {'media_url': settings.MEDIA_URL})

def new_view(request):
    context_dict = {'title': 'Welcome!', 'content': 'This is a new page using a template.'}
    return render(request, 'rango/new_template.html', context=context_dict)

def show_category(request, category_name_slug):
    context_dict = {}


    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)

        context_dict['category'] = category
        context_dict['pages'] = pages
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)



