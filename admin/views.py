from pages.models import Page, PageForm
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse


# Base processor
def base_processor(request):
    root_pages = Page.objects.filter(parent=None).all()
    return {'root_pages': root_pages}


# Index
def index(request):
    context = RequestContext(request, {
        'test': 'test',
    }, [base_processor])
    return render(request, 'admin/index.html', context)

# Media
def media(request):
    context = RequestContext(request, {
        'test': 'test',
    }, [base_processor])
    return render(request, 'admin/media.html', context)


# Edit
def edit(request, page_id=None):

    if page_id:
        page = get_object_or_404(Page, pk=page_id)
    else:
        page = Page()

    if request.POST:
        # A form bound to the POST data
        form = PageForm(request.POST, instance=page)

        if form.is_valid():
            page = form.save(commit=False)
            page.save()

            # Set message
            messages.success(request, 'The page is saved.')

    else:
        form = PageForm(instance=page)

    context = RequestContext(request, {
        'page': page,
        'form': form,
    }, [base_processor])

    return render(request, 'admin/edit.html', context)


# Delete
def delete(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    page.delete()
    return HttpResponse('1')


# Publish
def publish(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    page.published = 1
    page.save()
    return HttpResponse('1')


# Unpublish
def unpublish(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    page.published = 0
    page.save()
    return HttpResponse('1')
