from pages.models import Page
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404


# Index
def index(request):
    root_pages = Page.objects.filter(parent = None).all()
    context = {'root_pages' : root_pages}
    return render(request, 'pages/index.html', context)

# Detail
def detail(request, path):
    page = get_object_or_404(Page, path=path)
    context = {'page' : page}
    return render(request, 'pages/detail.html', context)
