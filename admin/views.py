from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse


# Index
def index(request):
    context = RequestContext(request, {
        'test': 'test',
    })
    return render(request, 'admin/index.html', context)