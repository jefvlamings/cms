from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView, View
from pages.models import Page, PageForm


# Index
class PagesIndexView(TemplateView):
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        context = super(PagesIndexView, self).get_context_data(**kwargs)
        context['root_pages'] = Page.objects.filter(parent=None).all()
        return context


# Detail
class PagesDetailView(TemplateView):
    template_name = "pages/detail.html"

    def get_context_data(self, **kwargs):
        context = super(PagesDetailView, self).get_context_data(**kwargs)
        context['page'] = get_object_or_404(Page, path=self.kwargs['path'])
        return context


# Create
class PagesCreateView(SuccessMessageMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = "pages/edit.html"
    success_message = "De pagina is aangemaakt."

    def get_success_url(self, **kwargs):
        return "."


# Update
class PagesUpdateView(SuccessMessageMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = "pages/edit.html"
    success_message = "De pagina is bijgewerkt."

    def get_success_url(self, **kwargs):
        return "./" + self.kwargs['pk']


# Delete
class PagesDeleteView(SuccessMessageMixin, DeleteView):
    model = Page
    success_message = "De pagina is verwijderd."


# Publish
class PagesPublishView(View):

    def get(self, request, **kwargs):
        page = get_object_or_404(Page, pk=self.kwargs['pk'])
        page.published = 1
        page.save()
        return HttpResponse('1')


# Unpublish
class PagesUnpublishView(View):

    def get(self, request, **kwargs):
        page = get_object_or_404(Page, pk=self.kwargs['pk'])
        page.published = 0
        page.save()
        return HttpResponse('1')

